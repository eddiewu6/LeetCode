


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        bytes = []
        for i in data:
            #check data larger than 255
            if i > 255:
                return False
            #modify bin if the len is less than 8
            temp = bin(i)[2:]
            if len(temp) < 8:
                for j in range(8 - len(temp)):
                    temp = "0" + temp
            bytes.append(temp)


        i = 0
        while i < len(bytes):
            if bytes[i][0] == "0":
                i += 1
            elif bytes[i][0:3] =="110":
                if i+1 >= len(bytes):
                    return False
                if bytes[i+1][0:2] != "10":
                    return False
                else:
                    i += 2
            elif bytes[i][0:4] == "1110":
                if i+1 >= len(bytes) or i+2 >= len(bytes):
                    return False
                if bytes[i+1][0:2] != "10" or bytes[i+2][0:2] != "10":
                    return False
                else:
                    i += 3
            elif bytes[i][0:5] == "11110":
                if i+1 >= len(bytes) or i+2 >= len(bytes) or i+3 >= len(bytes):
                    return False
                if bytes[i+1][0:2] != "10" or bytes[i+2][0:2] != "10" or bytes[i+3][0:2] != "10":
                    return False
                else:
                    i += 4
            else:
                return False
        return True
