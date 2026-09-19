month=input("enter month: ")
match month:
    case "may" | "june" | "july" :
        print("summer season")
    case "august" | "september" :
        print("rainy season")
    case "october" | "november" :
        print("autumn season") 
    case "december" | "january" :
        print("winter season") 
    case "february" | "march" |"april" :
        print("spring season")          
    case _:
        print("invalid month")