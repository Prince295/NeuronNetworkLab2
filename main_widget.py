import tkinter as interface
from widgets import *
from main import *
from tkinter.messagebox import *
import pickle


class MainWidget():
    def __init__(self, parent = None):
        button = []
        self.mainform = interface.Frame(parent)
        self.mainform.pack(fill = 'both', expand = True)

        form1 = Navs( self.mainform )
        form1.pack(fill = 'y')
        self.form2 = MainFrame( self.mainform )
        self.form2.pack()
        self.var3 = interface.StringVar()
        for i in range( 6 ):
            button.append( ThemedButton(form1) )
        button[0].config(text = "Добавить изображение",command = lambda : self.check_image())
        button[1].config(text = "Проверить изображение", command = lambda : self.check_check_image())
        button[2].config(text = "Обучить", command = lambda : learning(x,w1,w2,w3,sigma,h,e, output_error,e_error,t, t_error,b1,b2,b3))
        button[3].config(text = "Просмотр графика", command = lambda : show_graph())
        button[4].config( text= "Сохранить", command = lambda : self.save_collection() )
        button[5].config(text = "Открыть", command = lambda : self.open_collection())


        for i in range(len(button)):
            button[i].pack(in_ = form1, side = 'top', padx = 30, pady = 5)


    def check_check_image(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )

        entry = []
        black_button = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        labe11 = OutLabel(container1,text = "Результат")
        self.label2 = OutLabel(container1,text = self.var3.get(), bg = 'white')
        button1.config( text='Проверить', command=lambda: self.show_results(self.add_image(black_button),t,w1,w2,w3) )
        button1.pack(side = "top", padx = 20, pady = 20)
        labe11.pack(side = "top", padx = 5)
        self.label2.pack(side = "top", padx = 5)

        for i in range( 64 ):
            black_button.append( interface.Button( container2, width=3, height=1, bg='white', fg='black' ) )

        m = 0
        for i in range( 8 ):
            for j in range( 8 ):
                black_button[m].config( command=lambda m=m: self.change_color( black_button[m] ) )
                black_button[m].grid( row=i, column=j )
                m += 1
        container1.pack( side='bottom', fill='x', expand=True )
        container2.pack( side='bottom', fill='x', expand=True )

    def show_results(self,m, t, w1, w2, w3):
        for i in range( len( h[0] ) ):
            h[0][i] = activate_function( sum_func( m, w1[i] ), b1 )
            output_error[0][i] = activate_function( sum_func( x_mistakes[0], w1[i] ), b1 )
        for i in range( len( h[1] ) ):
            h[1][i] = activate_function( sum_func( h[0], w2[i] ), b2 )
            output_error[1][i] = activate_function( sum_func( output_error[0], w2[i] ), b2 )
        for i in range( len( h[2] ) ):
            h[2][i] = round( activate_function( sum_func( h[1], w3[i] ), b3 ), 3 )
            output_error[2][i] = round( activate_function( sum_func( output_error[1], w3[i] ), b3 ), 3 )

        self.var3.set("{0:.3f} , {1:.3f} , {2:.3f} , {3:.3f} ".format( h[2][0], h[2][1], h[2][2], h[2][3] ))
        self.label2.config(text = self.var3.get())

    def check_image(self):
        self.clear_form()
        form1 = Navs( self.form2, padx=0 )
        form1.pack( expand=True, fill="both" )
        form2 = Navs( self.form2, padx=0 )
        form2.pack( expand=True, fill="both" )
        label = []
        entry = []
        black_button = []

        container1 = Container( form1 )
        container2 = Container( form2 )
        button1 = CommandButton( container1 )
        button1.config( text='Добавить', command=lambda: self.find_image(black_button,var1.get()) )
        button1.pack(side = "top", padx = 20)
        var1 = interface.StringVar()
        classes = ThemedMenu(container1, var1, "K", "L", "M", "N")
        classes.pack(side = "top", padx = 20)
        var1.set("K")

        for i in range( 64 ):
            black_button.append(interface.Button(container2, width = 3, height = 1, bg = 'white', fg = 'black'))

        m=0
        for i in range(8):
            for j in range(8):
                black_button[m].config(command = lambda m = m : self.change_color(black_button[m]))
                black_button[m].grid(row = i, column = j)
                m+=1
        container1.pack( side='bottom', fill='x', expand=True )
        button1.pack( side='right', padx=0.5 )
        container2.pack( side='bottom', fill='x', expand=True )

    def change_color(self,button):

        if button['bg'] == 'white':
            button.config(bg = 'pink')
        else:
            button.config(bg = 'white')

    def add_image(self,button):
        exz = []
        letter_dict = {"K": [1, 0, 0, 0],
                       "L": [0, 1, 0, 0],
                       "M": [0, 0, 1, 0],
                       "N": [0, 0, 0, 1]}
        for i in range( len( button ) ):
            if button[i]['bg'] == 'white':
                exz.append( 0 )
            else:
                exz.append( 1 )
        return exz


    def find_image(self, button, letter):
        exz = []
        letter_dict = {"K" : [1,0,0,0],
                       "L" : [0,1,0,0],
                       "M" : [0,0,1,0],
                       "N" : [0,0,0,1]}
        for i in range(len(button)):
            if button[i]['bg'] == 'white':
                exz.append(0)
            else:
                exz.append(1)
        x.append(exz)
        t.append(letter_dict[letter])

    def clear_form(self):
        self.form2.destroy()
        self.form2 = MainFrame( self.mainform )
        self.form2.pack()

    def open_collection(self):
        global x
        global t
        global w1
        global w2
        global w3
        f1 = open( 'temp', 'rb' )

        x,t, w1, w2, w3 = pickle.load( f1 )


        f1.close()
        showinfo( "Открыто", "Успешно!" )



    def save_collection(self):
        f1 = open( 'temp', 'wb' )
        pickle.dump( [x,t,w1,w2,w3], f1 )
        f1.close()
        showinfo( "Сохраненено", "Успешно!" )

if __name__ == "__main__":
    root = interface.Tk()
    root.geometry( "800x600+100+100" )
    MainWidget( root )
    root.mainloop()