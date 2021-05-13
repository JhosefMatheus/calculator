class Calculator:
    def __init__(self):
        self.__num_1 = '0'
        self.__num_2 = '0'
        self.__screen = []
        self.__operations = ['+', '-', 'x', '/', '\u221a', 'x²', '1/x', '%', 'CE', 'C', '-/+', '=', '\u2190']
    
    def __is_operator(self, button):
        return button in self.__operations
    
    def __identify_operator(self, button):
        if button == '+':
            return '+'
        elif button == '-':
            return '-'
        elif button == 'x':
            return '*'
        elif button == '/':
            return '/'
        elif button == '\u221a':
            return '\u221a'
        elif button == 'x²':
            return '(1/2)**2'
        elif button == '1/x':
            return '1/x'
        elif button == '%':
            return '%'
        elif button == 'CE':
            return 'CE'
        elif button == 'C':
            return 'C'
        elif button == '-/+':
            return '-/+'
        elif button == '=':
            return '='
        elif button == '\u2190':
            return '\u2190'

    def button_click(self, button, label):
        if self.__is_operator(button):
            operator = self.__identify_operator(button)
            print(operator)
        
        else:
            self.__num_1 += button
            label['text'] = self.__num_1