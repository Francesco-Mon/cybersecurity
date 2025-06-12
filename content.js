document.addEventListener("click", function (e) {
  const link = e.target.closest("a");
  if (link && link.href) {
    const url = link.href;
    const check = isSuspicious(url);
    if (!check.safe) {
      e.preventDefault();
      showOverlay(url, check.reason);
    }
  }
});

function isSuspicious(url) {
  try {
    const suspiciousDomains = ["bit.ly", "tinyurl.com", "grabify.link"];
    const trustedBrands = [
      "example.com", "facebook.com", "google.com", "apple.com", "amazon.com",
      "paypal.com", "netflix.com", "linkedin.com", "instagram.com"
    ];

    const parsedUrl = new URL(url);
    const hostname = parsedUrl.hostname.replace(/^www\./, "");

    const reasons = [];

    if (parsedUrl.protocol === "http:") reasons.push("Connessione non sicura (http)");
    if (/^(\d{1,3}\.){3}\d{1,3}$/.test(parsedUrl.hostname)) reasons.push("IP diretto sospetto");
    if (suspiciousDomains.includes(hostname)) reasons.push("Shortener usato spesso per phishing");
    if (url.length > 150) reasons.push("URL eccessivamente lungo");
    if (/login|verify|update|secure/.test(url)) reasons.push("Parole chiave sospette nel dominio");

    // Verifica similitudine con domini noti (typosquatting)
    for (const brand of trustedBrands) {
      const distance = levenshtein(hostname, brand);
      if (distance > 0 && distance <= 2) {
        reasons.push(`Possibile imitazione di ${brand} (somiglianza sospetta: ${hostname})`);
        break;
      }
    }

    return {
      safe: reasons.length === 0,
      reason: reasons.join(", ")
    };
  } catch (err) {
    return { safe: true };
  }
}

function levenshtein(a, b) {
  const dp = Array.from({ length: a.length + 1 }, () => []);
  for (let i = 0; i <= a.length; i++) dp[i][0] = i;
  for (let j = 0; j <= b.length; j++) dp[0][j] = j;

  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      dp[i][j] = a[i - 1] === b[j - 1]
        ? dp[i - 1][j - 1]
        : 1 + Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]);
    }
  }

  return dp[a.length][b.length];
}

function showOverlay(url, reason) {
  if (document.getElementById("url-guardian-overlay")) return;

  const overlay = document.createElement("div");
  overlay.id = "url-guardian-overlay";
  overlay.innerHTML = `
    <div class="ug-modal">
      <h2>⚠️ Link potenzialmente pericoloso</h2>
      <p><strong>URL:</strong> <span class="ug-url">${url}</span></p>
      <p><strong>Motivo:</strong> ${reason}</p>
      <div class="ug-buttons">
        <button id="ug-proceed">Apri comunque</button>
        <button id="ug-cancel">Annulla</button>
      </div>
    </div>
  `;
  document.body.appendChild(overlay);

  document.getElementById("ug-proceed").onclick = () => {
    window.location.href = url;
  };
  document.getElementById("ug-cancel").onclick = () => {
    overlay.remove();
  };
}
