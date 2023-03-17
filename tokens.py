# Defines all base tokens

class Token:
    token_list = {
            "set":                      "=",
            "open_parentheses":         "(",
            "close_parentheses":        ")",
            "comma":                    ",",
            "dot":                      ".",
            "open_brackets":            "[",
            "close_brackets":           "]",
            "open_curly_brackets":      "{",
            "close_curly_brackets":     "}",
            "quote":                    "\"",
            "single_quote":             "\'",
            "equals":                   "==",
            "not_equals":               "!=",
            "greater_than":             ">",
            "greater_than_or_equal":    ">=",
            "less_than":                "<",
            "less_than_or_equal":       "<=",
            "question_mark":            "?",
            "star":                     "*",
            "plus":                     "+",
            "minus":                    "-",
            "divide":                   "/",
            "pointer_arrow":            "->",
    }
    
    def get(self, name):
        return self.token_list.get(name)

