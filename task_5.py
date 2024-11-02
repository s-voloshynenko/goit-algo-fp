from task_4 import build_heap_tree, draw_tree

def generate_color_gradient(num_colors):
    red_step = 25
    green_step = 10
    blue_step = 25

    colors = [
        f"#{min(255, 50 + i * red_step):02X}{min(255, 100 + i * green_step):02X}{max(0, 255 - i * blue_step):02X}"
        for i in range(num_colors)
    ]
    return colors

def dfs(tree_root):
    stack = [tree_root]
    visited_nodes = set()
    colors = generate_color_gradient(6)
    index = 0

    while stack:
        node = stack.pop()
        if node and node not in visited_nodes:
            node.color = colors[index % len(colors)]
            visited_nodes.add(node)
            index += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs(tree_root):
    queue = [tree_root]
    visited_nodes = set()
    colors = generate_color_gradient(6)
    index = 0

    while queue:
        node = queue.pop(0)
        if node and node not in visited_nodes:
            node.color = colors[index % len(colors)]
            visited_nodes.add(node)
            index += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

heap = [0, 1, 5, 3, 4, 10]
root = build_heap_tree(heap)

dfs(root)
draw_tree(root)

bfs(root)
draw_tree(root)
