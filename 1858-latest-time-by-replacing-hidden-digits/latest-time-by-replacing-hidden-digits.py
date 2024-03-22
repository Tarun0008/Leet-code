class Solution:
    def maximumTime(self, time: str) -> str:
        time_list = list(time)
        
      
        for i in range(len(time_list)):
            if time_list[i] == '?':
                if i == 0:
                    time_list[i] = '2' if time_list[i + 1] in ('?', '0', '1', '2', '3') else '1'
                elif i == 1:
                    time_list[i] = '3' if time_list[i - 1] == '2' else '9'
                elif i == 3:
                    time_list[i] = '5'
                elif i == 4:
                    time_list[i] = '9'
        
        # Join the list back into a string
        return ''.join(time_list)

        