<?php
$jsonPath = 'assets/data_sync.json';
if (!file_exists($jsonPath)) { die("Erro: JSON não encontrado."); }
$dados = json_decode(file_get_contents($jsonPath), true);

// Preparamos os dados para o Gráfico (JavaScript precisa de arrays)
$labels = [];
$valores = [];
foreach ($dados as $item) {
    $labels[] = $item['produto'];
    $valores[] = $item['valor_taxado'];
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Analytics Dev-Log</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; padding: 40px; background: #f4f7f6; }
        .container { max-width: 900px; margin: auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
        canvas { margin-top: 30px; max-height: 400px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 0.9em; }
        th { background: #ee4d2d; color: white; padding: 12px; text-align: left; }
        td { padding: 10px; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
	<?php
	// Verifica se o SQL está offline (simulação simples)
	$status_sistema = file_exists('assets/backup_recovery.csv') ? 'Modo de Segurança (Backup)' : 'Online (Direto do SQL)';
	$cor_status = ($status_sistema == 'Modo de Segurança (Backup)') ? '#ffcc00' : '#28a745';
	?>
	
	<div style="background: <?= $cor_status ?>; color: black; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 20px;">
	    STATUS DO SISTEMA: <?= $status_sistema ?>
	</div>
    <div class="container">
        <h1>📊 Analytics Dashboard</h1>
        <p>Integração: <strong>MySQL ➔ Python (Pandas) ➔ JSON ➔ PHP</strong></p>
        
        <canvas id="meuGrafico"></canvas>

        <table>
            <tr><th>Produto</th><th>Total com Taxa</th><th>Data</th></tr>
            <?php foreach ($dados as $item): ?>
            <tr>
                <td><?= $item['produto'] ?></td>
                <td>R$ <?= number_format($item['valor_taxado'], 2, ',', '.') ?></td>
                <td><?= $item['data_venda'] ?></td>
            </tr>
            <?php endforeach; ?>
        </table>
    </div>

    <script>
        const ctx = document.getElementById('meuGrafico');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: <?= json_encode($labels) ?>,
                datasets: [{
                    label: 'Valor de Vendas (R$)',
                    data: <?= json_encode($valores) ?>,
                    backgroundColor: 'rgba(238, 77, 45, 0.6)',
                    borderColor: 'rgba(238, 77, 45, 1)',
                    borderWidth: 1
                }]
            },
            options: { scales: { y: { beginAtZero: true } } }
        });
    </script>
</body>
</html>
