class Solution {
public:
    void bfs(vector<int>& edges, int node, vector<int>& dists){
        queue<int> q;
        q.push(node);
        dists[node] = 0;
        vector<bool> vd(edges.size());

        while(!q.empty()){
            int cur = q.front();
            q.pop();
            if(!vd[cur]){
                vd[cur] = true;
                int next = edges[cur];
                if(next!=-1 && !vd[next]){
                    dists[next] = dists[cur] + 1;
                    q.push(next);
                }
            }
        }
    }

    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        vector<int> dists1(edges.size(), numeric_limits<int>::max());
        vector<int> dists2(edges.size(), numeric_limits<int>::max());

        bfs(edges, node1, dists1);
        bfs(edges, node2, dists2);

        int minD = numeric_limits<int>::max();
        int minN = -1;

        for(int i=0; i<edges.size(); i++){
            if(minD > max(dists1[i], dists2[i])){
                minD = max(dists1[i], dists2[i]);
                minN = i;
            }
        }

        return minN;
    }
};
