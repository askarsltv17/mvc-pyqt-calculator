class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += str(char)

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            if not self.expression: return ""
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except ZeroDivisionError:
            return "Error: Div by 0"
        except Exception:
            return "Error"

    def get_expression(self):
        return self.expression