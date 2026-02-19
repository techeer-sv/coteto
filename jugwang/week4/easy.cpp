#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    
    vector<int>::iterator ptr;
    for (ptr = array.begin(); ptr != array.end(); ++ptr) {
        int num = *ptr;
        while(num != 0) {
            if (num %10 == 7) {
                answer++;
            }
            num /= 10;
        }
    }

    return answer;
}