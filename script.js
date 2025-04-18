
async function handleDownload() {
  const url = document.getElementById('urlInput').value;
  if (!url) return;

  document.getElementById('status').innerText = 'Verificando...';

  const res = await fetch('https://your-backend-url/api/download', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ url })
  });

  const data = await res.json();
  if (data.success) {
    document.getElementById('status').innerHTML = '<a href="' + data.download_url + '">Clique aqui para baixar</a>';
  } else {
    document.getElementById('status').innerText = 'Erro ao baixar: ' + data.message;
  }
}
