class DisjointSet {
private:
    vector<int> parent, size;

public:
    DisjointSet(int n){
        parent.resize(n);
        size.resize(n,1);
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
    }

    int find(int n){
        while(parent[n]!=n){
            n = parent[n];
        }
        return n;
    }

    void unionSet(int n1, int n2){
        n1 = find(n1);
        n2 = find(n2);
        if(parent[n1]==parent[n2]){
            return;
        }else if(size[n1]<size[n2]){
            parent[n1] = parent[n2];
            size[n2] += size[n1];
        }else{
            parent[n2] = parent[n1];
            size[n1] += size[n2];
        }
    }
};

class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int n = vals.size();
        vector<vector<int>> tree(n);

        for(auto& edge: edges){
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }

        map<int, vector<int>> vtn;
        for(int i=0; i<n; i++){
            vtn[vals[i]].push_back(i);
        }

        DisjointSet ds(n);
        int ans = 0;

        for(auto& [v,ns]: vtn){
            for(int n: ns){
                for(int adj: tree[n]){
                    if(vals[adj]<=vals[n]){
                        ds.unionSet(n,adj);
                    }
                }
            }

            unordered_map<int, int> g;
            for(int n: ns){
                g[ds.find(n)]++;
            }

            for(auto& [_,s]: g){
                ans += (s*(s+1)/2);
            }
        }

        return ans;
    }
};
