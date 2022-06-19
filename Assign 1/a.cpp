#include <bits/stdc++.h>
using namespace std;
int main() {
	int test;
	cin>>test;
	while(test--)
	{
		int x,y,z,k,i;
		cin>>x>>y>>z>>k;
		vector<int>vec(y);
		vector<int>printed;
		for(int i=0;i<y;++i)
		cin>>vec[i];
		sort(vec.begin(),vec.end());
		priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>pq;
		int currtime = 0;
		i=0;
		int j=0;
		while(i<x)
		{
			if(pq.empty())
			{
			pq.push(make_pair(vec[j],j));
			++j;
			++i;
			}
			else
			{
				if(j<y && pq.top().first>vec[j])
				{
					pq.push(make_pair(vec[j],j));
					++j;
					++i;
				}
				else
				{
					int currtime=pq.top().first;
					int currmachine=pq.top().second;
					printed.push_back(currtime);
					pq.pop();
					pq.push(make_pair(currtime+vec[currmachine],currmachine));
					++i;
				}
			}
		}
		while(!pq.empty())
		{
			printed.push_back(pq.top().first);
			pq.pop();
		}
		i=0;
		vector<int>finalvec;
		for(i=0;i<min((int)printed.size(),z);++i)
			pq.push(make_pair(printed[i]+k,1));
		while(i<printed.size())
		{
			finalvec.push_back(pq.top().first);
			currtime = max(pq.top().first,printed[i]);
			pq.pop();
			pq.push(make_pair(currtime+k,1));
			++i;
		}
		while(!pq.empty())
		{
			finalvec.push_back(pq.top().first);
			pq.pop();
		}
		cout<<"answer is "<<finalvec[finalvec.size()-1]<<endl;
	}
	return 0;
}