class SolutionLoop:
    from collections import OrderedDict
    def intToRoman(self, num: int) -> str:
        int_to_rom = OrderedDict({
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'        
        })
        
        s = ''
        for denom, char in int_to_rom.items():
            n, num = divmod(num, denom)
            s += n * char
            
        return s

class SolutionIndexing:
      
    def intToRoman(self, nums: int) -> str:
        M = ["","M","MM","MMM"]
        C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        return M[nums//1000] + C[(nums%1000)//100] + X [(nums%100)//10] + I[(nums%10)]