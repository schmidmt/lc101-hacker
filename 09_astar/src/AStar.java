import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;

public class AStar {

    private Grid grid;
    private PriorityQueue<Node> fringe;
    private HashSet<Node> seen;

    public AStar(Grid grid) {
        this.grid = grid;
        seen = new HashSet<>();
        fringe = new PriorityQueue<>();
        fringe.add(grid.getStart());
        seen.add(grid.getStart());
    }

    public ArrayList<Node> search() {
        while (fringe.size() > 0) {
            Node cur = fringe.poll();
            seen.add(cur);
            // System.out.println(cur);
            if (cur == grid.getStop()) {
                return unroll(cur);
            }
            ArrayList<Node> neighs = grid.getNeighbors(cur);
            for (Node neigh: neighs) {
                if (!seen.contains(neigh)) {
                    if (neigh.getDistTraveled() < 0) {
                        neigh.setDistTraveled(cur.getDistTraveled() + 1);
                        neigh.setPrev(cur);
                        fringe.add(neigh);
                    } else if (neigh.getDistTraveled() > cur.getDistTraveled() + 1) {
                        neigh.setDistTraveled(cur.getDistTraveled() + 1);
                        neigh.setPrev(cur);
                    }
                }
            }
        }
        return null;
    }

    private static ArrayList<Node> unroll(Node node) {
        ArrayList<Node> path = new ArrayList<>();
        Node cur = node;
        while (cur != null) {
            path.add(0, cur);
            cur = cur.getPrev();
        }
        return path;
    }

}
