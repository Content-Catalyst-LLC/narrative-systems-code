-- Four-function myth review queries.

SELECT
    item,
    claim_context,
    mystical_function,
    cosmological_function,
    sociological_function,
    pedagogical_function
FROM four_function_myth_claims
ORDER BY sociological_function DESC;
