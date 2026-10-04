const $ = id => document.getElementById(id), log = $("log"), input = $("q");
const esc = s => s.replace(/[&<>]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;"}[c]));
const fmt = s => esc(s).replace(/`([^`]+)`/g, "<code>$1</code>")
  .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>").replace(/\n/g, "<br>");

function add(txt, who, extra) {
  const d = document.createElement("div");
  d.className = "m " + who;
  d.innerHTML = fmt(txt) + (extra || "");
  log.appendChild(d); log.scrollTop = log.scrollHeight;
  return d;
}
async function ask(q) {
  q = q.trim(); if (!q) return;
  add(q, "user"); input.value = "";
  const t = document.createElement("div");
  t.className = "m bot"; t.innerHTML = '<span class="dots"><i></i><i></i><i></i></span>';
  log.appendChild(t); log.scrollTop = log.scrollHeight;
  try {
    const res = await fetch("/api/chat", {method: "POST",
      headers: {"Content-Type": "application/json"}, body: JSON.stringify({message: q})});
    const r = await res.json();
    await new Promise(ok => setTimeout(ok, 350));
    t.remove();
    if (!res.ok) { add(r.error || "Something went wrong.", "bot"); return; }
    const tag = r.topic ? '<span class="tag">From the knowledge base · ' + esc(r.topic) + "</span>" : "";
    add(r.answer, "bot", tag);
  } catch (e) {
    t.remove(); add("I couldn't connect to the assistant. Please check that the Flask server is running, then try again.", "bot");
  }
}
$("f").addEventListener("submit", e => { e.preventDefault(); ask(input.value); });
function start() {
  log.innerHTML = "";
  add("Hello. I'm AI-Chatbot, a knowledge-base assistant. Ask me about AI, machine learning, deep learning, programming or algorithms.", "bot");
}
$("clear").onclick = start; start();
