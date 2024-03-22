class Solution:
    def reformatNumber(self, number: str) -> str:
  
        number = number.replace(" ", "").replace("-", "")
    
        formatted_number = []
        while len(number) > 4:
            formatted_number.append(number[:3])
            number = number[3:]
    
        if len(number) == 2:
            formatted_number.append(number)
        elif len(number) == 3:
            formatted_number.append(number)
        elif len(number) == 4:
            formatted_number.append(number[:2])
            formatted_number.append(number[2:])
    
        return "-".join(formatted_number)
