# [Bronze III] 2017 아주대학교 프로그래밍 경시대회 (Small) - 14592 

[문제 링크](https://www.acmicpc.net/problem/14592) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 7월 31일 14:16:33

### 문제 설명

<p>아주대학교 프로그래밍 경시대회(Ajou Programming Contest, APC)는 2009년 제1회를 시작으로 2014년 제6회까지 개최된 아주대학교 학생들을 위한 프로그래밍 경시대회이다. 2017년, 다른 학교에서 활발히 진행되는 교내대회를 보던 현정이는 3년 만에 APC를 부활시키기로 결심했다.</p>

<p>2017 APC 운영 방식은 다음과 같다.</p>

<ul>
	<li>문제는 Small 데이터와 Large 데이터로 이루어져 있다.</li>
	<li>문제를 풀기 위해서는 입력 파일을 다운로드 받고, 5분 이내로 이에 맞는 출력 파일과 소스 코드를 업로드해야 한다.</li>
	<li>Small 데이터 문제를 해결해야 Large 데이터 입력 파일을 다운로드 받을 수 있다.</li>
	<li>각 문제의 Small, Large 데이터를 해결하면 점수를 얻을 수 있으며, 이 점수는 각각 다르다.</li>
	<li>제출 횟수는 점수를 획득한 문제를 맞기 까지 인풋을 다운로드 받은 횟수의 총합이다.</li>
	<li>즉, 점수를 획득하지 못한 문제의 다운로드 횟수는 포함되지 않는다.</li>
</ul>

<p>위 운영 방식에 따라 순위는 다음과 같이 결정된다.</p>

<ul>
	<li>해결한 문제 점수의 총합이 높은 참가자가 더 높은 순위를 가진다.</li>
	<li>점수의 총합이 같은 경우, 제출 횟수가 적은 참가자가 더 높은 순위를 가진다.</li>
	<li>점수의 총합과 제출 횟수가 같은 경우, 마지막으로 점수를 획득한 문제의 업로드 시간이 빠른 참가자가 더 높은 순위를 가진다.</li>
</ul>

<p>매우 유감스럽게도 현정이는 며칠째 잠을 제대로 자지 못해 흉폭해져있다. 현정이의 일을 덜어 잠깐이라도 잘 수 있도록 참가자들의 순위를 계산하는 프로그램을 작성해주자.</p>

### 입력 

 <p>첫 번째 줄에는 참가자의 수를 나타내는 자연수 N (1 ≤ N ≤ 3) 이 주어진다.</p>

<p>두 번째 줄부터 N 개의 줄에 걸쳐 세 개의 정수 S<sub>i</sub>, C<sub>i</sub>, L<sub>i</sub> (0 ≤ S<sub>i</sub> ≤ 620, 0 ≤ C<sub>i</sub> ≤ 50, 0 ≤ L<sub>i</sub> ≤ 179)가 주어진다.</p>

<p>(1+i) 번째 줄의 각 값은 차례로 i 번째 참가자의 점수, 제출 횟수, 마지막으로 점수를 획득한 문제의 업로드 시간을 나타낸다. 세 값이 모두 같은 참가자는 존재하지 않는다.</p>

### 출력 

 <p>1등을 하는 참가자의 번호를 한 줄에 출력한다.</p>

