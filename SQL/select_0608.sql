-- https://programmers.co.kr/learn/courses/30/lessons/59034?language=oracle
-- 모든 레코드 조회하기
-- mysql
-- oracle
SELECT * from animal_ins group by animal_id;
SELECT * from animal_ins order by animal_id

-- https://programmers.co.kr/learn/courses/30/lessons/59035
-- 역순 정렬하기
-- mysql
-- oracle
SELECT name,datetime from animal_ins order by animal_id desc

-- https://programmers.co.kr/learn/courses/30/lessons/59036
-- 아픈 동물찾기
-- mysql
-- oracle
SELECT animal_id, name from animal_ins 
where intake_condition = 'Sick'
order by animal_id

-- https://programmers.co.kr/learn/courses/30/lessons/59037
-- 어린 동물찾기
-- mysql
-- oracle
SELECT animal_id, name from animal_ins
where intake_condition <> 'Aged'
order by animal_id

SELECT animal_id, name from animal_ins
where not intake_condition = 'Aged'
order by animal_id

