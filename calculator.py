class Calculator:
    def __init__(self):
        self.__num_1 = ''
        self.__num_2 = ''
        self.__operator = None
        self.__operations = ['+', '-', 'x', '/', 'CE', 'C', '=', '\u2190']
    
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
        elif button == '=':
            return '='
        elif button == 'CE':
            return 'CE'
        elif button == 'C':
            return 'C'
        elif button == '\u2190':
            return 'backspace'
        

    def button_click(self, button, label):
        if self.__is_operator(button):
            if self.__identify_operator(button) != '=':
                self.__operator = self.__identify_operator(button)
                print(f'Operator: {self.__operator}')
            
            else:
                result = eval(f'{self.__num_1} {self.__operator} {self.__num_2}')
                label['text'] = result
                self.__num_1 = ''
                self.__num_2 = ''
                self.__operator = None
        
        else:
            if self.__operator is None:
                self.__num_1 += button
                label['text'] = self.__num_1
            else:
                self.__num_2 += button
                label['text'] = self.__num_2
            print(f'Number: {button}')