#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream f("date.in");
ofstream g("date.out");

int main(){

    int n,m,c[100][100];
    int t[100][100],prev[100];


    f>>n>>m;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++){
            f>>t[i][j];
            c[i-1][j-1]=0;
            c[i+1][j-1]=0;
            c[i][j]=0;
        }

    for(int j=1;j<=m;j++)
        for(int i=1;i<=n;i++){
            c[i][j] = max(c[i-1][j-1],max(c[i][j-1],c[i+1][j-1]))+t[i][j];
                if( max(c[i-1][j-1],max(c[i][j-1],c[i+1][j-1])) == c[i-1][j-1])
                    prev[c[i][j]] = 3;
                if( max(c[i-1][j-1],max(c[i][j-1],c[i+1][j-1])) == c[i][j-1])
                    prev[c[i][j]] = 2;
                if( max(c[i-1][j-1],max(c[i][j-1],c[i+1][j-1])) == c[i+1][j-1])
                    prev[c[i][j]] = 1;

        }

    for(int i=1;i<=n;i++){
        prev[t[i][1]] = 0;
    }

    int maxi = 0,ii=0,jj=0, ok=0;
    for(int j=1;j<=n;j++){
        if(c[j][m] == maxi) ok=1;
        if(c[j][m] > maxi){
            maxi = c[j][m];
            ii=j;
            jj=m;
            ok=0;
        }
    }

    g<<maxi<<endl;
    int traseu[n*m];
    for( int i=0; i<n*m; i++)
        traseu[i]=0;
    int poz=0;
    traseu[poz]=ii;
    poz++;
    traseu[poz]=jj;
    poz++;
    while(prev[maxi] != 0){
        jj--;
        if(prev[maxi] == 1)
            ii++;
        if(prev[maxi] == 3)
            ii--;
        maxi = c[ii][jj];
        traseu[poz]=ii;
        poz++;
        traseu[poz]=jj;
        poz++;
    }
    poz = 0;
    while(traseu[poz]!=0)
        poz++;
    poz--;
    while(poz>=0)
    {g<<traseu[poz-1]<<' '<<traseu[poz]<<endl;
    poz-=2;
    }
    if(ok==0) g<<"Solutie unica";
        else g<<"Solutia nu este unica";


}

