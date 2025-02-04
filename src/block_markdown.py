block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordlist = "ordered_list"
block_type_unordlist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks_list = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block: # This ensures only non-empty blocks are added. Simply it uses Python's implicit truthiness. Empty strings evaluate to False in conditional statements.
            blocks_list.append(stripped_block)
    return blocks_list

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordlist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordlist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordlist
    return block_type_paragraph
