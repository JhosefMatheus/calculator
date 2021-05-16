class Calculator:
    def __init__(self):
        self.__num_1 = ''
        self.__num_2 = ''
        self.__operator = None
        self.__operations = ['+', '-', 'x', '/', 'CE', 'C', '=', '\u2190']
        self.__first_time = True
    
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
        elif button == 'C':
            return 'C'
        

    def button_click(self, button, label):
        if self.__is_operator(button):
            if self.__identify_operator(button) != '=':
                if self.__identify_operator(button) != 'C':
                    self.__operator = self.__identify_operator(button)
                    self.__num_1 = label['text']
                    self.__first_time = True
                    print(f'Operator: {self.__operator}')
                else:
                    label['text'] = '0'
                    self.__first_time = True
            
            else:
                try:
                    print(self.__num_1, self.__num_2)
                    self.__num_2 = label['text']
                    result = eval(f'{self.__num_1} {self.__operator} {self.__num_2}')
                    label['text'] = result
                    # self.__num_1 = ''
                    # self.__num_2 = ''
                    # self.__first_time = True
                    # self.__operator = None
                except Exception as error:
                    print(error)
                    label['text'] = 'Error'
                finally:
                    self.__num_1 = ''
                    self.__num_2 = ''
                    self.__first_time = True
                    self.__operator = None
        
        else:
            if self.__operator is None:
                if self.__first_time:
                    label['text'] = button
                    self.__first_time = False
                else:
                    label['text'] += button
                # self.__num_1 += button
                # label['text'] = self.__num_1
            else:
                if self.__first_time:
                    label['text'] = button
                    self.__first_time = False
                else:
                    label['text'] += button
                # self.__num_2 += button
                # label['text'] = self.__num_2
            print(f'Number: {button}')