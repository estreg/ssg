import re
from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

                                                                        
def split_nodes_delimiter(old_nodes, delimiter, text_type):             
    result_list = []
    for node in old_nodes:                                              
        if node.text_type != TextType.TEXT:
            result_list.append(node)

        else:
            nodes_list = node.text.split(delimiter)
            if len(nodes_list) % 2 == 0:
                raise Exception(f"Invalid markdown syntax: missing closing {delimiter}")

            for index, piece in enumerate(nodes_list):
                if index % 2 != 0:
                    code_node = TextNode(piece, text_type)
                    result_list.append(code_node)
                else:
                    if piece: # This check is very important! otherwise the code could produce empty nodes, which could lead to rendering issues later.
                        new_text_node = TextNode(piece, TextType.TEXT)
                        result_list.append(new_text_node)
    return result_list

def split_nodes_image(old_nodes): 
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
        
        else:
            images = extract_markdown_images(node.text) # "Images" contains the result of your function operating on "node.text".
            if len(images) == 0:
                result_list.append(node)

            else:
                for image in images:
                    sections = node.text.split(f"![{image[0]}]({image[1]})", 1)                           
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, image section not closed")
                    if sections[0] != "":
                        result_list.append(TextNode(sections[0], TextType.TEXT))                          
                    result_list.append(TextNode(image[0], TextType.IMAGE, image[1],))
                    node.text = sections[1]
                if node.text != "":
                    result_list.append(TextNode(node.text, TextType.TEXT))                                                                
    return result_list

def split_nodes_link(old_nodes): 
    result_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_list.append(node)
        
        else:
            links = extract_markdown_links(node.text) # "Links" contains the result of your function operating on "node.text".
            if len(links) == 0:
                result_list.append(node)

            else:
                for link in links:
                    sections = node.text.split(f"[{link[0]}]({link[1]})", 1)                           
                    if len(sections) != 2:
                        raise ValueError("Invalid markdown, link section not closed")
                    if sections[0] != "":
                        result_list.append(TextNode(sections[0], TextType.TEXT))                          
                    result_list.append(TextNode(link[0], TextType.LINK, link[1]))
                    node.text = sections[1]
                if node.text != "":
                    result_list.append(TextNode(node.text, TextType.TEXT))                                                                
    return result_list

def text_to_textnodes(text):
    processed_nodes = [TextNode(text, TextType.TEXT)]
    processed_nodes = split_nodes_image(processed_nodes)
    processed_nodes = split_nodes_link(processed_nodes)
    processed_nodes = split_nodes_delimiter(processed_nodes, "**", TextType.BOLD)
    processed_nodes = split_nodes_delimiter(processed_nodes, "*", TextType.ITALIC)
    processed_nodes = split_nodes_delimiter(processed_nodes, "`", TextType.CODE)
    return processed_nodes