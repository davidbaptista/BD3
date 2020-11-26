--1. Qual o concelho onde se fez o maior volume de vendas hoje?

SELECT c.nome, sum(quant * preco) volume_de_venda
FROM concelho c
JOIN instituicao i ON c.num_concelho = i.num_concelho AND c.num_regiao = i.num_regiao
JOIN venda_farmacia v ON i.nome = v.inst
WHERE v.data_registo = current_date
GROUP BY c.nome
HAVING sum(quant * preco) >= ALL
    (SELECT sum(quant * preco)
    FROM concelho co
    JOIN instituicao it ON co.num_concelho = it.num_concelho
    JOIN venda_farmacia ve ON it.nome = ve.inst
    WHERE ve.data_registo = current_date
    GROUP BY co.nome);

--2. Qual o médico que mais prescreveu no 1o semestre de 2019 em cada região?

WITH query_name AS (SELECT m.nome, r.nome AS regiao, COUNT(c.num_doente) AS prescricoes
	FROM medico m
	JOIN prescricao p ON m.num_cedula = p.num_cedula
	JOIN consulta c ON p.num_cedula = c.num_cedula AND p.num_doente = c.num_doente AND p.data_consulta = c.data_consulta
	JOIN instituicao i ON c.nome_instituicao = i.nome
	JOIN regiao r ON i.num_regiao = r.num_regiao
	WHERE EXTRACT(MONTH FROM c.data_consulta) IN ('1','2','3','4','5','6')
	AND EXTRACT(YEAR FROM c.data_consulta) = '2019'
	GROUP BY m.nome, r.nome)
SELECT regiao, nome, prescricoes FROM (
	SELECT regiao, MAX(prescricoes) AS prescricoes
	FROM query_name
	AS result
	GROUP BY regiao)
AS A1
NATURAL JOIN query_name;

--3. Quais são os médicos que já prescreveram aspirina em receitas aviadas em todas as farmácias do concelho de Arouca este ano?

SELECT nome FROM medico
WHERE NOT EXISTS (
	SELECT DISTINCT i.nome
	FROM instituicao i JOIN concelho c ON c.num_concelho = i.num_concelho AND c.num_regiao = i.num_regiao
	WHERE LOWER(c.nome) = 'arouca' AND LOWER(i.tipo) = 'farmacia'
	EXCEPT 
	SELECT DISTINCT inst FROM (
		SELECT m.nome, v.num_venda, v.inst
			FROM prescricao_venda p
			JOIN venda_farmacia v ON v.num_venda = p.num_venda AND v.substancia = p.substancia
			JOIN instituicao i ON i.nome = v.inst
			JOIN concelho c ON c.num_concelho = i.num_concelho AND c.num_regiao = i.num_regiao
			JOIN medico m ON p.num_cedula = m.num_cedula
			WHERE EXTRACT(YEAR FROM v.data_registo) = EXTRACT(YEAR FROM current_date)
			AND LOWER(c.nome) = 'arouca' AND LOWER(p.substancia) = 'aspirina'
	) AS result
	WHERE nome = medico.nome
);

--4. Quais são os doentes que já fizeram análises mas ainda não aviaram prescrições este mês?

SELECT a.num_doente FROM analise a
WHERE EXTRACT(MONTH FROM a.data_registo) = EXTRACT(MONTH FROM current_date) 
AND NOT EXISTS (
	SELECT p.num_doente
	FROM prescricao_venda p NATURAL JOIN venda_farmacia v
	WHERE EXTRACT(MONTH FROM data_registo) = EXTRACT(MONTH FROM current_date)
	AND p.num_doente = a.num_doente
);
