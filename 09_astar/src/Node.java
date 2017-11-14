public class Node implements Comparable<Node> {

    private int x, y, distTraveled, distToGoEstimated;
    private Node prev;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
        distTraveled = -1;
        distToGoEstimated = 0;
        prev = null;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getDistTraveled() {
        return distTraveled;
    }

    public void setDistTraveled(int distTraveled) {
        this.distTraveled = distTraveled;
    }

    public int getDistToGoEstimated() {
        return distToGoEstimated;
    }
    public void setDistToGoEstimated(Node end) {
        this.setDistToGoEstimated(Math.abs(x - end.x) + Math.abs(y - end.y));
    }

    public void setDistToGoEstimated(int distToGoEstimated) {
        this.distToGoEstimated = distToGoEstimated;
    }

    public int getDist() {
        return distToGoEstimated + distTraveled;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.getDist(), o.getDist());
    }

    public Node getPrev() {
        return prev;
    }

    public void setPrev(Node prev) {
        this.prev = prev;
    }

    @Override
    public String toString() {
        return "Node(" + x + ", " + y +")";
    }
}
