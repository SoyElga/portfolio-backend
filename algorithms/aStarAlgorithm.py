class Node:
    father = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_f_cost(self, x0, y0, xf, yf):
        g = abs(x0-self.x)+abs(y0-self.y)
        h = abs(xf-self.x)+abs(yf-self.y)

        self.Fcost = g + h

    def evaluate_position(self, xf, yf):
        return self.x == xf and self.y == yf

def get_min_f_cost_node_index(node_list):
    f_costs = [node.Fcost for node in node_list]
    return f_costs.index(min(f_costs))

def a_star_algorithm(map, start, end):
    node_map = []
    for y, row in enumerate(map):
        nrow = []
        for x, _ in enumerate(row):
            n = Node(x, y)
            nrow.append(n)
        node_map.append(nrow)

    map_size = (len(node_map[0]), len(node_map))

    open = [] #List with all yet to check nodes
    closed = [] #List with all checked nodes

    start_node = node_map[start[1]][start[0]]
    start_node.calculate_f_cost(start[1], start[0], end[1], end[0])
    open.append(start_node)

    while len(open) > 0:
        current_node = open.pop(get_min_f_cost_node_index(open))
        closed.append(current_node)

        if current_node.evaluate_position(end[0], end[1]):
            return current_node
        else:
            neighbors = []
            for n in (-1, 1):
                if 0 <= current_node.y + n < map_size[1]:
                    if map[current_node.y + n][current_node.x] == 0 and not node_map[current_node.y + n][current_node.x] in closed:
                        neighbors.append(node_map[current_node.y + n][current_node.x])
                if 0 <= current_node.x + n < map_size[0]:
                    if not map[current_node.y][current_node.x + n] == 1 and not node_map[current_node.y][current_node.x + n] in closed:
                        neighbors.append(node_map[current_node.y][current_node.x + n])
            
            for n in neighbors:
                if not n in open:
                    n.father = current_node
                    n.calculate_f_cost(start[1], start[0], end[1], end[0])
                    open.append(n)
    return "No route has been found"