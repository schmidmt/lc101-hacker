import java.util.ArrayList;
import java.util.HashSet;
import java.util.InputMismatchException;

public class Grid {

    private Node[][] grid;
    private int width, height;
    private Node start;
    private Node stop;

    public Grid(String asciiArt) {
        width = asciiArt.indexOf("\n");
        height = (int) asciiArt.chars().filter(x -> x == '\n').count();

        grid = new Node[width][height];

        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                char cur = asciiArt.charAt(x + y * (width + 1));
                switch (cur) {
                    case '#':
                        break;
                    case 'S':
                        grid[x][y] = new Node(x, y);
                        start = grid[x][y];
                        break;
                    case 'E':
                        grid[x][y] = new Node(x, y);
                        stop = grid[x][y];
                        break;
                    case ' ':
                        grid[x][y] = new Node(x, y);
                        break;
                    default:
                        throw new InputMismatchException("Got '" + cur + "' which shouldn't happen!");
                }
            }
        }

        start.setDistTraveled(0);

        // Initialize distances
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                Node cur = this.get(x, y);
                if (cur != null) {
                    cur.setDistToGoEstimated(stop);
                }
            }
        }
    }

    public Node get(int x, int y) {
        if (x < 0 || x > width || y < 0 || y > height) { return null; }
        return grid[x][y];
    }

    public Node getStop() {
        return stop;
    }

    public ArrayList<Node> getNeighbors(Node node) {
        return getNeighbors(node.getX(), node.getY());
    }

    public ArrayList<Node> getNeighbors(int x, int y) {
        ArrayList<Node> neighs = new ArrayList<>();
        Node neigh;

        neigh = this.get(x - 1, y);
        if (neigh != null) {
            neighs.add(neigh);
        }
        neigh = this.get(x + 1, y);
        if (neigh != null) {
            neighs.add(neigh);
        }
        neigh = this.get(x, y - 1);
        if (neigh != null) {
            neighs.add(neigh);
        }
        neigh = this.get(x, y + 1);
        if (neigh != null) {
            neighs.add(neigh);
        }
        return neighs;
    }

    public Node getStart() {
        return start;
    }

    public void print(ArrayList<Node> path) {
        HashSet<Node> pathNodes = new HashSet<>(path);

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Node cur = this.get(x, y);
                if (cur == null) {
                    System.out.print('#');
                } else {
                    if (pathNodes.contains(cur)) {
                        System.out.print('*');
                    } else {
                        System.out.print(' ');
                    }
                }
            }
            System.out.print('\n');
        }
    }
}
