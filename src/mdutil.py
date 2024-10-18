from src.constants import *

def block_to_block_type(markdown):
    match(markdown[0]):
        case "#":
            return MD_TYPE_H

