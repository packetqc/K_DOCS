---
layout: publication
page_type: interface
title: "Claude Interface"
description: "AI-powered development environment with integrated knowledge tools, live mindmap, and command navigation."
pub_id: "Interface I6"
version: "v1"
date: "2026-03-17"
permalink: /interfaces/claude-interface/
keywords: "claude, ai, chat, api, mindmap, tools, commands, development"
dev_banner: "Interface in development — requires API key configuration. Features and layout may change between sessions."
---

# Claude Interface

{::nomarkdown}

<style>
/* ═══ Claude Interface variables ═══ */
:root {
  --ci-chat-bg: #f8f6f2;
  --ci-user-bg: #e8e4f0;
  --ci-assistant-bg: #ffffff;
  --ci-input-bg: #ffffff;
  --ci-input-border: #c8c4d0;
  --ci-success: #16a34a;
  --ci-tool-bg: #f0ece4;
  --ci-sidebar-bg: #f4f0ea;
  --ci-sidebar-w: 280px;
}
[data-theme="midnight"], [data-theme="dark"] {
  --ci-chat-bg: #1e1e2e;
  --ci-user-bg: #2a2a3e;
  --ci-assistant-bg: #24243a;
  --ci-input-bg: #2a2a3e;
  --ci-input-border: #444466;
  --ci-success: #4ade80;
  --ci-tool-bg: #2a2a3e;
  --ci-sidebar-bg: #1a1a2e;
}

/* ═══ Safe area — extend into notch/status bar area on mobile ═══ */
@supports (padding-top: env(safe-area-inset-top)) {
  .ci-root {
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
  }
}

/* ═══ Layout ═══ */
.ci-root {
  display: flex; height: calc(100vh - 2rem); gap: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg, #faf6f1); color: var(--fg, #1a1a2e);
}
.ci-main { flex: 1; display: flex; flex-direction: column; min-width: 0; }
.ci-sidebar {
  width: var(--ci-sidebar-w, 280px); background: var(--ci-sidebar-bg, #f4f0ea);
  border-left: 1px solid var(--border, #d48a3c); display: flex; flex-direction: column;
  overflow-y: auto; flex-shrink: 0;
}

/* ═══ Toolbar ═══ */
.ci-toolbar {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.4rem 0.75rem; background: var(--code-bg, #eee8df);
  border-bottom: 1px solid var(--border, #d48a3c); flex-shrink: 0;
}
.ci-toolbar-title { font-weight: 600; font-size: 0.85rem; color: var(--fg, #1a1a2e); }
.ci-toolbar-spacer { flex: 1; }
.ci-status {
  font-size: 0.7rem; padding: 0.15rem 0.5rem; border-radius: 9px;
  background: var(--ci-tool-bg, #f0ece4); color: var(--muted, #5c5c78);
}
.ci-status.connected { color: var(--ci-success, #16a34a); font-weight: 600; }

/* ═══ Chat area ═══ */
.ci-chat {
  flex: 1; overflow-y: auto; padding: 1rem; display: flex; flex-direction: column; gap: 0.75rem;
  background: var(--ci-chat-bg, #f8f6f2);
}
.ci-msg {
  max-width: 85%; padding: 0.65rem 0.9rem; border-radius: 0.6rem;
  font-size: 0.85rem; line-height: 1.5; white-space: pre-wrap; word-break: break-word;
}
.ci-msg.user {
  align-self: flex-end; background: var(--ci-user-bg, #e8e4f0);
  border-bottom-right-radius: 0.15rem;
}
.ci-msg.assistant {
  align-self: flex-start; background: var(--ci-assistant-bg, #ffffff);
  border: 1px solid var(--border, #d48a3c); border-bottom-left-radius: 0.15rem;
}
.ci-msg.system {
  align-self: center; font-size: 0.75rem; color: var(--muted, #5c5c78);
  font-style: italic; max-width: 100%;
}
.ci-msg code { background: var(--code-bg, #eee8df); padding: 0.1rem 0.3rem; border-radius: 3px; font-size: 0.8rem; }
.ci-msg pre { background: var(--code-bg, #eee8df); padding: 0.5rem; border-radius: 4px; overflow-x: auto; margin: 0.4rem 0; }
.ci-msg pre code { background: none; padding: 0; }

/* ═══ Input area ═══ */
.ci-input-area {
  display: flex; gap: 0.5rem; padding: 0.6rem 0.75rem;
  background: var(--code-bg, #eee8df); border-top: 1px solid var(--border, #d48a3c);
  flex-shrink: 0;
}
.ci-input {
  flex: 1; padding: 0.5rem 0.75rem; border: 1px solid var(--ci-input-border, #c8c4d0);
  border-radius: 0.4rem; background: var(--ci-input-bg, #ffffff); color: var(--fg, #1a1a2e);
  font-size: 0.85rem; font-family: inherit; resize: none; min-height: 2.2rem; max-height: 8rem;
}
.ci-input:focus { outline: none; border-color: var(--accent, #0055b3); box-shadow: 0 0 0 2px rgba(0,85,179,0.15); }
.ci-send-btn {
  padding: 0.5rem 1rem; background: var(--accent, #0055b3); color: #fff;
  border: none; border-radius: 0.4rem; font-size: 0.85rem; font-weight: 600;
  cursor: pointer; white-space: nowrap; align-self: flex-end;
}
.ci-send-btn:hover { opacity: 0.9; }
.ci-send-btn:disabled { opacity: 0.5; cursor: not-allowed; }

/* ═══ Sidebar ═══ */
.ci-sb-section { padding: 0.6rem 0.75rem; border-bottom: 1px solid var(--border, #d48a3c); }
.ci-sb-title {
  font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
  color: var(--muted, #5c5c78); letter-spacing: 0.04em; margin-bottom: 0.4rem;
}
.ci-sb-item {
  display: block; padding: 0.3rem 0.5rem; font-size: 0.78rem; border-radius: 4px;
  color: var(--fg, #1a1a2e); text-decoration: none; cursor: pointer;
  transition: background 0.15s;
}
.ci-sb-item:hover { background: var(--col-alt, rgba(0,85,179,0.05)); }
.ci-sb-item code { font-size: 0.72rem; background: var(--code-bg, #eee8df); padding: 0.05rem 0.25rem; border-radius: 3px; }

/* ═══ Mindmap embed ═══ */
.ci-mindmap-frame {
  flex: 1; min-height: 200px; border: none; width: 100%;
  background: var(--ci-sidebar-bg, #f4f0ea);
}

/* ═══ Setup overlay ═══ */
.ci-setup {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  flex: 1; padding: 2rem; text-align: center; gap: 1rem;
}
.ci-setup h2 { font-size: 1.1rem; color: var(--fg, #1a1a2e); margin: 0; }
.ci-setup p { font-size: 0.85rem; color: var(--muted, #5c5c78); max-width: 400px; margin: 0; }
.ci-key-input {
  width: 100%; max-width: 380px; padding: 0.5rem 0.75rem;
  border: 1px solid var(--ci-input-border, #c8c4d0); border-radius: 0.4rem;
  background: var(--ci-input-bg, #ffffff); color: var(--fg, #1a1a2e);
  font-size: 0.85rem; font-family: monospace;
}
.ci-key-btn {
  padding: 0.5rem 1.5rem; background: var(--accent, #0055b3); color: #fff;
  border: none; border-radius: 0.4rem; font-weight: 600; cursor: pointer;
}
.ci-key-btn:hover { opacity: 0.9; }
.ci-key-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.ci-key-note { font-size: 0.72rem; color: var(--muted, #5c5c78); }
.ci-provider-group {
  display: flex; gap: 0.5rem; width: 100%; max-width: 380px; justify-content: center;
}
.ci-provider-btn {
  flex: 1; padding: 0.5rem 0.4rem; border: 2px solid var(--border, #d48a3c);
  border-radius: 0.4rem; background: var(--ci-input-bg, #ffffff); color: var(--fg, #1a1a2e);
  font-size: 0.75rem; font-weight: 600; cursor: pointer; text-align: center;
  transition: border-color 0.15s, background 0.15s;
}
.ci-provider-btn:hover { border-color: var(--accent, #0055b3); }
.ci-provider-btn.active {
  border-color: var(--accent, #0055b3); background: var(--col-alt, rgba(0,85,179,0.05));
}
.ci-get-key {
  font-size: 0.78rem; color: var(--accent, #0055b3); text-decoration: none;
}
.ci-get-key:hover { text-decoration: underline; }
.ci-validate-msg {
  font-size: 0.75rem; min-height: 1.1em;
}
.ci-validate-msg.ok { color: var(--ci-success, #16a34a); }
.ci-validate-msg.err { color: #dc2626; }

/* ═══ Development banner ═══ */
.ci-dev-banner {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.5rem 1rem; flex-shrink: 0;
  background: #fffbeb; border-bottom: 1px solid #fde68a;
  color: #92400e; font-size: 0.8rem; line-height: 1.4;
}
[data-theme="midnight"] .ci-dev-banner,
[data-theme="dark"] .ci-dev-banner {
  background: #451a03; border-color: #92400e; color: #fde68a;
}
.ci-dev-banner-icon { font-size: 1rem; flex-shrink: 0; }

/* ═══ Responsive ═══ */
@media (max-width: 700px) {
  .ci-sidebar { display: none; }
}
</style>

<div class="ci-root" id="ci-viewer" data-baseurl="{{ site.baseurl }}">

  <!-- ── Main panel ── -->
  <div class="ci-main">
    <div class="ci-toolbar">
      <span class="ci-toolbar-title">Claude Interface</span>
      <span class="ci-toolbar-spacer"></span>
      <span class="ci-status" id="ci-status">disconnected</span>
      <a class="iface-info-btn" data-pub="guide-claude-interface" title="User Guide">&#8505;</a>
    </div>

    <div class="ci-dev-banner">
      <span class="ci-dev-banner-icon">&#9888;</span>
      <span><strong>Development Build</strong> — Claude Interface is under active development. Features and layout may change between sessions.</span>
    </div>

    <!-- Setup screen (shown when no API key) -->
    <div class="ci-setup" id="ci-setup">
      <h2>Claude Interface</h2>
      <p>AI-powered development environment with integrated knowledge tools, live mindmap, and command navigation.</p>

      <div class="ci-provider-group">
        <button class="ci-provider-btn active" data-provider="anthropic">Anthropic API</button>
        <button class="ci-provider-btn" data-provider="bedrock">AWS Bedrock</button>
        <button class="ci-provider-btn" data-provider="vertex">Google Vertex</button>
      </div>

      <input type="password" class="ci-key-input" id="ci-key-input" placeholder="sk-ant-api03-...">
      <div id="ci-provider-fields" style="display:none; width:100%; max-width:380px;">
        <input type="text" class="ci-key-input" id="ci-region-input" placeholder="Region (e.g. us-east-1)" style="margin-bottom:0.4rem;">
      </div>

      <button class="ci-key-btn" id="ci-key-btn">Connect</button>
      <span class="ci-validate-msg" id="ci-validate-msg"></span>

      <a class="ci-get-key" id="ci-get-key" href="https://console.anthropic.com/settings/keys" target="_blank" rel="noopener">Get an API key from Anthropic Console</a>
      <span class="ci-key-note">Key is stored in localStorage only — never sent anywhere except the selected provider API. Clear anytime via the disconnect button.</span>
    </div>

    <!-- Chat (hidden until connected) -->
    <div class="ci-chat" id="ci-chat" style="display:none;"></div>
    <div class="ci-input-area" id="ci-input-area" style="display:none;">
      <textarea class="ci-input" id="ci-input" rows="1" placeholder="Message Claude..."></textarea>
      <button class="ci-send-btn" id="ci-send-btn">Send</button>
    </div>
  </div>

  <!-- ── Sidebar ── -->
  <div class="ci-sidebar" id="ci-sidebar">

    <div class="ci-sb-section">
      <div class="ci-sb-title" id="ci-sb-tools-title">Quick Tools</div>
      <div id="ci-sb-tools">
        <a class="ci-sb-item" data-cmd="status"><code>status</code> Current state</a>
        <a class="ci-sb-item" data-cmd="recall"><code>recall</code> Deep memory search</a>
        <a class="ci-sb-item" data-cmd="pub list"><code>pub list</code> Publications</a>
        <a class="ci-sb-item" data-cmd="project list"><code>project list</code> Projects</a>
        <a class="ci-sb-item" data-cmd="harvest --list"><code>harvest --list</code> Harvest status</a>
        <a class="ci-sb-item" data-cmd="normalize"><code>normalize</code> Structure audit</a>
        <a class="ci-sb-item" data-cmd="help"><code>help</code> All commands</a>
      </div>
    </div>

    <div class="ci-sb-section">
      <div class="ci-sb-title" id="ci-sb-nav-title">Navigation</div>
      <div id="ci-sb-nav">
        <a class="ci-sb-item" data-nav="session-review">Session Review</a>
        <a class="ci-sb-item" data-nav="task-workflow">Tasks Workflow</a>
        <a class="ci-sb-item" data-nav="project-viewer">Project Viewer</a>
        <a class="ci-sb-item" data-nav="live-mindmap">Live Mindmap</a>
      </div>
    </div>

    <div class="ci-sb-section" style="flex:1; display:flex; flex-direction:column; min-height:200px;">
      <div class="ci-sb-title" id="ci-sb-mindmap-title">Live Mindmap</div>
      <iframe class="ci-mindmap-frame" id="ci-mindmap-frame"></iframe>
    </div>

  </div>
</div>

<!-- ═══ ℹ button handler ═══ -->
<style>.iface-info-btn{display:inline-flex;align-items:center;justify-content:center;width:1.5rem;height:1.5rem;border-radius:50%;background:var(--accent,#1d4ed8);color:#fff;font-size:0.85rem;font-weight:700;text-decoration:none;cursor:pointer;flex-shrink:0;margin-left:0.25rem;}.iface-info-btn:hover{opacity:0.85;}</style>
<script>
(function(){
  var btn = document.querySelector('.iface-info-btn');
  if (!btn) return;
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    var slug = this.dataset.pub;
    var lp = (document.documentElement.lang === 'fr' || location.pathname.indexOf('/fr/') >= 0) ? '/fr' : '';
    var base = (typeof viewerRewriteUrl === 'function') ? '' : '{{ "" | relative_url }}';
    var pubUrl = base + lp + '/publications/' + slug + '/full/';
    if (window.parent !== window && window.name === 'center-frame') {
      window.parent.postMessage({ type: 'open-pub', url: pubUrl, title: 'Claude Interface Guide' }, '*');
    } else {
      window.open(pubUrl, '_blank');
    }
  });
})();
</script>

<!-- ═══ Main logic ═══ -->
<script>
(function() {
  'use strict';

  /* ── L10n ── */
  var lang = (document.documentElement.lang === 'fr'
    || window.location.pathname.indexOf('/fr/') !== -1) ? 'fr' : 'en';
  var L = {
    en: {
      title: 'Claude Interface',
      send: 'Send',
      placeholder: 'Message Claude...',
      connected: 'connected',
      disconnected: 'disconnected',
      streaming: 'streaming...',
      tools: 'Quick Tools',
      nav: 'Navigation',
      mindmap: 'Live Mindmap',
      welcome: 'Connected to Claude API. Type a message or click a quick tool to begin.',
      apiError: 'API error: ',
      networkError: 'Network error — check your connection and API key.',
      disconnect: 'Disconnect',
      clearKey: 'Clear API key and disconnect?',
      validating: 'Validating key...',
      validOk: 'Key validated successfully.',
      validFail: 'Invalid key — ',
      getKey: 'Get an API key from Anthropic Console',
      getKeyBedrock: 'Configure AWS Bedrock credentials',
      getKeyVertex: 'Configure Google Vertex AI credentials',
      placeholderAnthropic: 'sk-ant-api03-...',
      placeholderBedrock: 'AWS access key or session token',
      placeholderVertex: 'Google API key or service account token'
    },
    fr: {
      title: 'Interface Claude',
      send: 'Envoyer',
      placeholder: 'Message a Claude...',
      connected: 'connecte',
      disconnected: 'deconnecte',
      streaming: 'en cours...',
      tools: 'Outils rapides',
      nav: 'Navigation',
      mindmap: 'Mindmap vivant',
      welcome: 'Connecte a l\'API Claude. Tapez un message ou cliquez un outil pour commencer.',
      apiError: 'Erreur API : ',
      networkError: 'Erreur reseau — verifiez votre connexion et cle API.',
      disconnect: 'Deconnecter',
      clearKey: 'Effacer la cle API et deconnecter ?',
      validating: 'Validation de la cle...',
      validOk: 'Cle validee avec succes.',
      validFail: 'Cle invalide — ',
      getKey: 'Obtenir une cle API depuis Anthropic Console',
      getKeyBedrock: 'Configurer les identifiants AWS Bedrock',
      getKeyVertex: 'Configurer les identifiants Google Vertex AI',
      placeholderAnthropic: 'sk-ant-api03-...',
      placeholderBedrock: 'Cle d\'acces AWS ou jeton de session',
      placeholderVertex: 'Cle API Google ou jeton de compte de service'
    }
  };
  var t = L[lang] || L.en;

  /* ── DOM refs ── */
  var setup    = document.getElementById('ci-setup');
  var chat     = document.getElementById('ci-chat');
  var inputArea = document.getElementById('ci-input-area');
  var input    = document.getElementById('ci-input');
  var sendBtn  = document.getElementById('ci-send-btn');
  var status   = document.getElementById('ci-status');
  var keyInput = document.getElementById('ci-key-input');
  var keyBtn   = document.getElementById('ci-key-btn');
  var validateMsg = document.getElementById('ci-validate-msg');
  var getKeyLink  = document.getElementById('ci-get-key');
  var regionInput = document.getElementById('ci-region-input');
  var providerFields = document.getElementById('ci-provider-fields');
  var mindmapFrame = document.getElementById('ci-mindmap-frame');

  /* ── Apply L10n ── */
  sendBtn.textContent = t.send;
  input.placeholder = t.placeholder;
  var sbToolsTitle = document.getElementById('ci-sb-tools-title');
  var sbNavTitle   = document.getElementById('ci-sb-nav-title');
  var sbMmTitle    = document.getElementById('ci-sb-mindmap-title');
  if (sbToolsTitle) sbToolsTitle.textContent = t.tools;
  if (sbNavTitle)   sbNavTitle.textContent = t.nav;
  if (sbMmTitle)    sbMmTitle.textContent = t.mindmap;
  if (getKeyLink)   getKeyLink.textContent = t.getKey;

  /* ── State ── */
  var API_KEY_STORE = 'ci-anthropic-key';
  var PROVIDER_STORE = 'ci-provider';
  var REGION_STORE = 'ci-region';
  var messages = []; /* conversation history for API */
  var streaming = false;
  var activeProvider = localStorage.getItem(PROVIDER_STORE) || 'anthropic';

  /* ── Provider config ── */
  var PROVIDERS = {
    anthropic: {
      url: 'https://api.anthropic.com/v1/messages',
      model: 'claude-sonnet-4-6',
      headers: function(key) {
        return {
          'Content-Type': 'application/json',
          'x-api-key': key,
          'anthropic-version': '2023-06-01',
          'anthropic-dangerous-direct-browser-access': 'true'
        };
      },
      getKeyUrl: 'https://console.anthropic.com/settings/keys',
      placeholder: t.placeholderAnthropic,
      getKeyLabel: t.getKey,
      needsRegion: false
    },
    bedrock: {
      url: function(region) {
        return 'https://bedrock-runtime.' + (region || 'us-east-1') + '.amazonaws.com/model/anthropic.claude-sonnet-4-6-v1/invoke';
      },
      model: 'anthropic.claude-sonnet-4-6-v1',
      headers: function(key) {
        return {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + key
        };
      },
      getKeyUrl: 'https://console.aws.amazon.com/bedrock/',
      placeholder: t.placeholderBedrock,
      getKeyLabel: t.getKeyBedrock,
      needsRegion: true
    },
    vertex: {
      url: function(region) {
        return 'https://' + (region || 'us-central1') + '-aiplatform.googleapis.com/v1/projects/-/locations/' + (region || 'us-central1') + '/publishers/anthropic/models/claude-sonnet-4-6:rawPredict';
      },
      model: 'claude-sonnet-4-6',
      headers: function(key) {
        return {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + key
        };
      },
      getKeyUrl: 'https://console.cloud.google.com/vertex-ai',
      placeholder: t.placeholderVertex,
      getKeyLabel: t.getKeyVertex,
      needsRegion: true
    }
  };

  /* ── Provider switching ── */
  function setProvider(name) {
    activeProvider = name;
    localStorage.setItem(PROVIDER_STORE, name);
    var cfg = PROVIDERS[name];
    document.querySelectorAll('.ci-provider-btn').forEach(function(b) {
      b.classList.toggle('active', b.dataset.provider === name);
    });
    keyInput.placeholder = cfg.placeholder;
    if (getKeyLink) {
      getKeyLink.textContent = cfg.getKeyLabel;
      getKeyLink.href = cfg.getKeyUrl;
    }
    providerFields.style.display = cfg.needsRegion ? 'block' : 'none';
    validateMsg.textContent = '';
    validateMsg.className = 'ci-validate-msg';
  }

  document.querySelectorAll('.ci-provider-btn').forEach(function(btn) {
    btn.addEventListener('click', function() { setProvider(this.dataset.provider); });
  });

  /* ── Mindmap sidebar ── */
  function loadMindmap() {
    if (!mindmapFrame) return;
    var base = document.getElementById('ci-viewer').dataset.baseurl || '';
    var lp = lang === 'fr' ? '/fr' : '';
    mindmapFrame.src = base + lp + '/interfaces/live-mindmap/';
  }

  /* ── API key management ── */
  function getKey() { return localStorage.getItem(API_KEY_STORE) || ''; }
  function setKey(k) { localStorage.setItem(API_KEY_STORE, k); }
  function getRegion() { return localStorage.getItem(REGION_STORE) || ''; }
  function setRegion(r) { localStorage.setItem(REGION_STORE, r); }
  function clearKey() {
    localStorage.removeItem(API_KEY_STORE);
    localStorage.removeItem(PROVIDER_STORE);
    localStorage.removeItem(REGION_STORE);
  }

  function showChat() {
    setup.style.display = 'none';
    chat.style.display = 'flex';
    inputArea.style.display = 'flex';
    status.textContent = t.connected;
    status.classList.add('connected');
    addMsg('system', t.welcome);
    loadMindmap();
    input.focus();
  }

  function showSetup() {
    setup.style.display = 'flex';
    chat.style.display = 'none';
    inputArea.style.display = 'none';
    status.textContent = t.disconnected;
    status.classList.remove('connected');
  }

  /* ── Message rendering ── */
  function addMsg(role, text) {
    var div = document.createElement('div');
    div.className = 'ci-msg ' + role;
    /* Basic markdown-lite: code blocks and inline code */
    var html = text
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
      .replace(/`([^`]+)`/g, '<code>$1</code>');
    div.innerHTML = html;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    return div;
  }

  function updateMsg(div, text) {
    var html = text
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
      .replace(/`([^`]+)`/g, '<code>$1</code>');
    div.innerHTML = html;
    chat.scrollTop = chat.scrollHeight;
  }

  /* ── Build API request for active provider ── */
  function buildRequest(msgs, maxTokens) {
    var cfg = PROVIDERS[activeProvider];
    var key = getKey();
    var region = getRegion();
    var url = typeof cfg.url === 'function' ? cfg.url(region) : cfg.url;
    var headers = cfg.headers(key);
    var body = {
      model: typeof cfg.model === 'string' ? cfg.model : cfg.model,
      max_tokens: maxTokens || 4096,
      system: 'You are Claude, an AI assistant integrated into the Knowledge platform. You help with documentation, project management, code review, and knowledge work. Be concise and helpful. When the user sends a command name (like "status", "recall", "pub list"), explain what the command does and how to use it in the Claude Code CLI.',
      messages: msgs
    };
    /* Anthropic uses anthropic_version in body for Bedrock/Vertex */
    if (activeProvider !== 'anthropic') {
      body.anthropic_version = '2023-06-01';
    }
    return { url: url, headers: headers, body: body };
  }

  /* ── Validate API key with a minimal call ── */
  function validateKey(key, callback) {
    validateMsg.textContent = t.validating;
    validateMsg.className = 'ci-validate-msg';
    keyBtn.disabled = true;

    var region = regionInput ? regionInput.value.trim() : '';
    if (region) setRegion(region);

    /* Temporarily store key for buildRequest */
    setKey(key);
    var req = buildRequest([{ role: 'user', content: 'Hi' }], 16);

    fetch(req.url, {
      method: 'POST',
      headers: req.headers,
      body: JSON.stringify(req.body)
    })
    .then(function(res) {
      if (!res.ok) {
        return res.json().then(function(err) {
          throw new Error(err.error && err.error.message || 'HTTP ' + res.status);
        });
      }
      return res.json();
    })
    .then(function() {
      validateMsg.textContent = t.validOk;
      validateMsg.className = 'ci-validate-msg ok';
      callback(true);
    })
    .catch(function(err) {
      validateMsg.textContent = t.validFail + (err.message || 'unknown error');
      validateMsg.className = 'ci-validate-msg err';
      localStorage.removeItem(API_KEY_STORE);
      callback(false);
    })
    .finally(function() {
      keyBtn.disabled = false;
    });
  }

  /* ── Claude API call ── */
  function callClaude(userMsg) {
    if (streaming) return;
    streaming = true;
    sendBtn.disabled = true;
    status.textContent = t.streaming;

    messages.push({ role: 'user', content: userMsg });
    addMsg('user', userMsg);

    var assistantDiv = addMsg('assistant', '...');
    var fullText = '';
    var req = buildRequest(messages);

    fetch(req.url, {
      method: 'POST',
      headers: req.headers,
      body: JSON.stringify(req.body)
    })
    .then(function(res) {
      if (!res.ok) {
        return res.json().then(function(err) {
          throw new Error(t.apiError + (err.error && err.error.message || res.status));
        });
      }
      return res.json();
    })
    .then(function(data) {
      var content = data.content && data.content[0] && data.content[0].text || '(empty response)';
      fullText = content;
      updateMsg(assistantDiv, fullText);
      messages.push({ role: 'assistant', content: fullText });
    })
    .catch(function(err) {
      var errMsg = err.message || t.networkError;
      updateMsg(assistantDiv, errMsg);
      /* Remove failed user message from history */
      messages.pop();
    })
    .finally(function() {
      streaming = false;
      sendBtn.disabled = false;
      status.textContent = t.connected;
      status.classList.add('connected');
      input.focus();
    });
  }

  /* ── Event handlers ── */
  keyBtn.addEventListener('click', function() {
    var k = keyInput.value.trim();
    if (!k) return;
    validateKey(k, function(valid) {
      if (valid) {
        keyInput.value = '';
        showChat();
      }
    });
  });
  keyInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') keyBtn.click();
  });

  sendBtn.addEventListener('click', function() {
    var msg = input.value.trim();
    if (!msg || streaming) return;
    input.value = '';
    input.style.height = 'auto';
    callClaude(msg);
  });
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendBtn.click();
    }
  });
  /* Auto-resize textarea */
  input.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 128) + 'px';
  });

  /* Status click = disconnect */
  status.addEventListener('click', function() {
    if (!getKey()) return;
    if (confirm(t.clearKey)) {
      clearKey();
      messages = [];
      chat.innerHTML = '';
      showSetup();
    }
  });
  status.style.cursor = 'pointer';
  status.title = t.disconnect;

  /* Quick tools — inject command as user message */
  document.querySelectorAll('[data-cmd]').forEach(function(el) {
    el.addEventListener('click', function(e) {
      e.preventDefault();
      if (!getKey()) return;
      callClaude(this.dataset.cmd);
    });
  });

  /* Navigation — open interface in parent center frame */
  document.querySelectorAll('[data-nav]').forEach(function(el) {
    el.addEventListener('click', function(e) {
      e.preventDefault();
      var slug = this.dataset.nav;
      var base = document.getElementById('ci-viewer').dataset.baseurl || '';
      var lp = lang === 'fr' ? '/fr' : '';
      var url = base + lp + '/interfaces/' + slug + '/';
      if (window.parent !== window && window.name === 'center-frame') {
        window.parent.document.getElementById('center-frame-el').src = url;
      } else {
        window.location.href = url;
      }
    });
  });

  /* ── Init ── */
  setProvider(activeProvider);
  if (regionInput && getRegion()) regionInput.value = getRegion();
  if (getKey()) {
    showChat();
  } else {
    showSetup();
  }

})();
</script>

{:/nomarkdown}
