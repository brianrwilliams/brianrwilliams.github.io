// assets/latest-commit.js
// Client-side widget: fetch latest commit for a public GitHub repo and render it.
// Configure owner/repo/branch below.

(function () {
  const owner = "YOUR_GITHUB_USERNAME_OR_ORG"; // <-- change this
  const repo  = "YOUR_REPO_NAME";               // <-- change this
  const branch = "main";                        // <-- change if needed

  // ID of the container element to render into
  const CONTAINER_ID = "latest-commit";

  function escapeHtml(s) {
    return s ? s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])) : '';
  }

  async function fetchLatest() {
    const url = `https://api.github.com/repos/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}/commits?sha=${encodeURIComponent(branch)}&per_page=1`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("GitHub API responded " + res.status);
    const data = await res.json();
    if (!Array.isArray(data) || data.length === 0) throw new Error("No commits found");
    return data[0];
  }

  function render(container, commit) {
    const message = (commit.commit && commit.commit.message) ? commit.commit.message.split("\n")[0] : "(no message)";
    const authorName = (commit.commit && commit.commit.author && commit.commit.author.name) ? commit.commit.author.name : (commit.author && commit.author.login) || "unknown";
    const dateISO = commit.commit && commit.commit.author && commit.commit.author.date;
    const date = dateISO ? new Date(dateISO) : null;
    const sha = commit.sha ? commit.sha.slice(0, 7) : "";
    const commitUrl = commit.html_url || `https://github.com/${owner}/${repo}/commit/${commit.sha}`;

    container.innerHTML = `
      <div style="font-weight:600;margin-bottom:0.25rem;">
        <a href="${commitUrl}" target="_blank" rel="noopener noreferrer">${escapeHtml(message)}</a>
      </div>
      <div style="font-size:0.9rem;color:#444;">
        <span>${escapeHtml(authorName)}</span>
        <span style="margin:0 0.5rem;color:#999">•</span>
        <time datetime="${escapeHtml(dateISO || '')}">${date ? date.toLocaleString() : "unknown date"}</time>
        <span style="margin-left:0.5rem;color:#999">(${escapeHtml(sha)})</span>
      </div>
    `;
  }

  async function init() {
    const container = document.getElementById(CONTAINER_ID);
    if (!container) return;
    container.textContent = "Loading latest commit…";
    try {
      const commit = await fetchLatest();
      render(container, commit);
    } catch (err) {
      container.textContent = "Error loading latest commit: " + err.message;
      console.error("latest-commit widget error:", err);
    }
  }

  // Run when DOM is ready. If script is loaded with defer, this will run after parse.
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
