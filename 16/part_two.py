# Advent of Code 2021
# https://adventofcode.com/2021
# Day 16: Packet Decoder

from functools import reduce
from operator import add, mul, gt, lt, eq

class BITSDecoder:

    def __init__(self, hex_message: str) -> None:
        bin_message = self.hex_to_bin(hex_message)
        message_length = len(bin_message)
        self.scan_pos = 0
        self.packets_version_sum = 0
        while self.scan_pos < message_length - 11: # 11 is the minimum packet length (6 header + 5 literal value)
            self.transmission_value = self.transmition_value = self.recursively_scan_packets(bin_message)

    def hex_to_bin(self, message: str) -> None:
        str_list = []
        for i in message:
            str_list.append(bin(int(i, 16))[2:].zfill(4))
        return "".join(str_list)
    
    def recursively_scan_packets(self, message: str) -> int:
        version = int(message[self.scan_pos : self.scan_pos+3], 2)
        self.packets_version_sum += version
        type_ID = int(message[self.scan_pos+3 : self.scan_pos+6], 2)
        self.scan_pos += 6
        if type_ID == 4: # literal value
            return self.get_literal_value(message)
        else: # operator
            length_type_ID = int(message[self.scan_pos])
            self.scan_pos += 1
            args = []
            if length_type_ID: # = 1
                subpackets_number = int(message[self.scan_pos : self.scan_pos+11], 2)
                self.scan_pos += 11
                counter = 0
                for _ in range(subpackets_number):
                    args.append(self.recursively_scan_packets(message))
            else: # = 0
                subpackets_length = int(message[self.scan_pos : self.scan_pos+15], 2)
                self.scan_pos += 15
                start_pos = self.scan_pos
                while self.scan_pos - start_pos < subpackets_length:
                    args.append(self.recursively_scan_packets(message))
            if type_ID == 0:
                return reduce(add, args)
            elif type_ID == 1:
                return reduce(mul, args)
            elif type_ID == 2:
                return min(args)
            elif type_ID == 3:
                return max(args)
            elif type_ID == 5:
                return int(reduce(gt, args))
            elif type_ID == 6:
                return int(reduce(lt, args))
            elif type_ID == 7:
                return int(reduce(eq, args))
    
    def get_literal_value(self, data: str) -> int:
        last_group = False
        value = []
        while not last_group:
            if data[self.scan_pos] == "0":
                last_group = True
            value.append(data[self.scan_pos+1 : self.scan_pos+5])
            self.scan_pos += 5
        return int("".join(value), 2)


if __name__ == '__main__':
    with open("input.txt") as file:
        for line in file:
            message = line.rstrip()
            # print(message)
            decoder = BITSDecoder(message)
            print(decoder.transmission_value)

