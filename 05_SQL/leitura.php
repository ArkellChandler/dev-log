<?php
// Silenciar avisos técnicos
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Caminho absoluto para o banco de dados
$caminhoBanco = 'C:\Users\User\dev-log\05_SQL\estudos.db';

// Conectar ao banco SQLite3
$db = new SQLite3($caminhoBanco);

// Tentar buscar os dados
$resultado = $db->query("SELECT * FROM alunos");

if ($resultado) {
    echo "--- LISTA DE ALUNOS ---\n";
    $encontrou = false;
    while ($linha = $resultado->fetchArray(SQLITE3_ASSOC)) {
        echo "ID: " . $linha['id'] . " | Nome: " . $linha['nome'] . " | Nota: " . $linha['nota'] . "\n";
        $encontrou = true;
    }
    if (!$encontrou) {
        echo "Nenhum aluno cadastrado na tabela.\n";
    }
    echo "-----------------------\n";
} else {
    echo "Erro técnico: " . $db->lastErrorMsg() . "\n";
}
?>