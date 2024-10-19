from src.constants import *

def block_to_block_type(markdown):
    match(markdown[0]):
        case "#":
            pounds = markdown.count("#")
            if 1 <= pounds <= 6:
                return MD_TYPE_H
        case "`":
            if markdown[:3] == "```" and markdown[:3] == markdown[-3:]:
                return MD_TYPE_CODE
        case ">":
            quotes = markdown.split("\n")
            for line in quotes:
                if line[0] != ">":
                    return MD_TYPE_P
            return MD_TYPE_QUOTE
        case "*":
            unordered_list = markdown.split("\n")
            for line in unordered_list:
                if line[0:2] != "* ":
                    return MD_TYPE_P
            return MD_TYPE_UL
        case "-":
            unordered_list = markdown.split("\n")
            for line in unordered_list:
                if line[0:2] != "- ":
                    return MD_TYPE_P
            return MD_TYPE_UL
        case "1":
            ordered_list = markdown.split("\n")
            for idx, line in enumerate(ordered_list):
                if line[0:3] != f"{idx+1}. ":
                    return MD_TYPE_P
            return MD_TYPE_OL
                

    return MD_TYPE_P
