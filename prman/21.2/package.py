name = "prman"

version = "21.2"

description = "Renderman Pro Server"

tools = [
    "prman"
]

def commands():
    env.PATH.prepend("/opt/pixar/RenderManProServer-21.2/bin")
