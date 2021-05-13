class Calculator:
    def __init__(self):
        self.__screen = []
        self.__operations = ['+', '-', 'x', '/', '\u221a', 'x²', '1/x', '%', 'CE', 'C', '-/+', '=', '\u2190']

    def button_click(self, button, label):
        if label['text'] == '0' and button == '0':
            print(f'screen: {self.__screen}')
            pass

        elif label['text'] == '0' and button == '.':
            self.__screen.append('0.')
            print(f'screen: {self.__screen}')
        
        elif button not in self.__operations and len(self.__screen) == 0:
            self.__screen.append(button)
            label['text'] = self.__screen[0]
            print(f'screen: {self.__screen}')
        
        elif button not in self.__operations and len(self.__screen) == 1:
            n = self.__screen[0] + button
            self.__screen[0] = n
            label['text'] = self.__screen[0]
            print(f'screen: {self.__screen}')
        
        elif button in self.__operations and len(self.__screen) == 0:
            print(f'screen: {self.__screen}')
            pass

        elif button in self.__operations and len(self.__screen) == 1:
            self.__screen.append(button)
            label['text'] = '0'
            print(f'screen: {self.__screen}')
        
        elif button not in self.__operations and len(self.__screen) == 2:
            self.__screen.append(button)
            label['text'] = self.__screen[2]
            print(f'screen: {self.__screen}')
        
        elif button not in self.__operations and len(self.__screen) == 3:
            n = self.__screen[2] + button
            self.__screen[2] = n
            label['text'] = self.__screen[2]
            print(f'screen: {self.__screen}')

        elif button in self.__operations and len(self.__screen) == 3:
            n = eval(f'{self.__screen[0]} {self.__screen[1]} {self.__screen[2]}')
            print(n)
            self.__screen = [str(n)]
            label['text'] = self.__screen[0]
            print(f'screen: {self.__screen}')