from graphviz_static import *
import os
import subprocess

load_paths()


dot_content = """
digraph G {
    node [shape=box, style=filled, color=lightblue];
    sigma sigma -> "ligma ligma" -> "scam scam";
}
"""

with open("test_dot_file.dot", "w", encoding="utf-8") as f:
    f.write(dot_content)

print("Drawing, wait...")

export_to_image("test_dot_file.dot", "png", "output")