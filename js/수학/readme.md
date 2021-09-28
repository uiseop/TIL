# 알고리즘 복잡도 (시간 복잡도를 중점으로)


- 평가지표 : 2개가 코테에서 가장 중요시 여기더라
    - 정확성
    - 작업량
    - `메모리 사용량`
    - 최적성
    - `효율성`
- 입력 크기의 값에 대해 단위 연산을 몇 번 수행하는지 계산하여, 알고리즘의 수행시간을 평가하는 방법
- 빅오 : `최악의 상황을` 고려하여 측정
- 세타 : `평균적인` 경우
- 오메가 : `최선의 상황일` 때의 성능

# 경우의 수

- 순열 : n개의 원소중에 r개를 중복없이 골라 순서에 `상관 있게` Permutations
    - nPr = n! / (n-r)! 으로 표현
    - 가령 A,B,C 👉 A,B,C / A,C,B / B,A,C / B,C,A / C,A,B/ C,B,A : 총 6가지
    - `for문을` 통해 하는방법 / 👍👍`재귀로` 하는 방법
    ```
    let input = ['a','b','c']
    let count = 0
    // s : from, r : to
    function permutation(arr,s,r){
        // 재귀를 멈출 기저조건
        if(s == r){
            count += 1
            console.log(arr.join(" "))
            return
        }
        // 재귀를 돌면서 변경되어야 될 부분
        for(let i=s; i< arr.length; i++){
            [arr[s], arr[i]] = [arr[i],arr[s]]
            permutation(arr,s+1,r)
            [arr[s], arr[i]] = [arr[i],arr[s]]
        }
    }
    ```
- 조합 : 순서에 `상관 없게` Combinations
- 중복 순열 : `중복이 가능하게`! 단, 순서에도 `상관이 있어` -> 카카오 21년 블라인드 테스트에 나왔지!?

# 점화식

- DP(Dynamic Programing)문제를 풀 때 사용되더라.
- 점화식(재귀식)이란 수열에서 이웃하는 두개의 항 사이에 `성립하는 관계를` 찾는 관계식!