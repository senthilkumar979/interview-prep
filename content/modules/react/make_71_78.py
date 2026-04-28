import json
from pathlib import Path

L = lambda label, href: [{"label": label, "href": href}]
E = lambda title, code, exp, lang="tsx": {"title": title, "language": lang, "code": code, "explanation": exp}
ROOT = Path(__file__).resolve().parent

ITEMS: list[dict] = [
    {
        "id": "react-071",
        "question": "What is Module Federation in the React ecosystem?",
        "difficulty": "intermediate",
        "category": "mfe",
        "tags": ["module-federation", "micro-frontend", "webpack"],
        "answer": "**Module Federation** (a **Webpack 5** feature; other bundlers can achieve similar **runtime** loading patterns) allows a **host** application to **import** a **remote** JavaScript build at **runtime** and, when the **shared** config is correct, use **one** physical copy of `react` and `react-dom` in the page.\n\n**Why it matters to React teams:** orgs can ship **independently** deployed areas of the UI in one **shell** without a single monolithic build for every **vertical**. The real work is **version** alignment, **router** strategy, and **isolation** of styles and **side effects**, not a single `import` call.\n",
        "examples": [E("Conceptual (Webpack)", "remotes: { mfe1: 'mfe1@https://.../remoteEntry.js' }\n", "Exact keys depend on the plugin—always read the version of **Module Federation** you ship.", "text")],
        "tip": "Pin **React** with **package.json** `overrides` / `resolutions` so every MFE build resolves the **same** major.\n",
        "links": L("Webpack: Module Federation", "https://webpack.js.org/concepts/module-federation/"),
    },
    {
        "id": "react-072",
        "question": "What is a hydration mismatch?",
        "difficulty": "intermediate",
        "category": "ssr",
        "tags": ["hydration", "ssr", "mismatch"],
        "answer": "During **hydration**, React walks the **server-emitted** HTML and tries to **attach** event listeners to the same logical tree the client components render. A **mismatch** means the first client render and the **existing** server markup **disagree** in a way that would require **rewriting** a node, so you see a **warning** in development.\n\n**Typical causes:** `Date.now()` in render, `Math.random()` for **visible** text or ids, **locale** differences, or **stale** cached HTML vs fresh API data on the first paint.\n",
        "examples": [E("Bad: random in render", "function Bad() {\n  return <span>{Math.random()}</span>;\n}\n", "Server and client pick different values; use `useId` or set non-determinism in `useEffect` when needed.", "tsx")],
        "tip": "Fix the **root** (deterministic render) before trying to **suppress** the warning—hiding the message often hides a **data** race.\n",
        "links": L("React: Resolving hydration errors (legacy doc)", "https://legacy.reactjs.org/docs/react-dom.html#hydrate"),
    },
    {
        "id": "react-073",
        "question": "What are React Server Components (RSC) at a high level?",
        "difficulty": "intermediate",
        "category": "ssr",
        "tags": ["rsc", "server-components", "nextjs"],
        "answer": "**Server Components** run only on the **server** and can **read** data sources, files, and secrets **without** that code shipping to the browser. The wire format streams **UI descriptions**; **Client Components** (declared in frameworks with the appropriate directive) own **interactivity**—`useState`, `useEffect`, and browser-only APIs—after hydration.\n",
        "examples": [E("Mental model", "// Server: fetch user on the wire\n// Client: 'use client' form with local validation\n", "Exact file syntax is defined by the **framework** (for example the Next.js **App** Router) you use.", "text")],
        "tip": "RSC is not a drop-in for every `useEffect` fetch: align **data boundaries** with your framework’s router and **cache** story.\n",
        "links": L("React: Server Components", "https://react.dev/reference/rsc/server-components"),
    },
    {
        "id": "react-074",
        "question": "What is Fast Refresh in development?",
        "difficulty": "beginner",
        "category": "tooling",
        "tags": ["fast-refresh", "hmr", "vite"],
        "answer": "**Fast Refresh** hot-replaces the module you edit so most **edits to JSX and hooks** apply **without a full page reload** and often **preserve** local component **state** when the change is **compatible** with the rules. **Vite** and similar dev servers wrap **`@vitejs/plugin-react`**, which uses the **`react-refresh`** Babel transform under the hood.\n",
        "examples": [E("Vite", "npm run dev\n", "A normal dev server command; the plugin wires Fast Refresh for you on save.", "bash")],
        "tip": "If state resets after a save, the edit may not be *refresh safe* (for example, you changed a component **type** in a way that remounts the subtree).\n",
        "links": L("Vite: React plugin", "https://github.com/vitejs/vite-plugin-react"),
    },
    {
        "id": "react-075",
        "question": "What are common ways to reduce React bundle size?",
        "difficulty": "intermediate",
        "category": "performance",
        "tags": ["bundle", "code-split", "import"],
        "answer": "Split with **`React.lazy` / dynamic** `import()` for **route** and **tab** code, use **per-function** imports from **large** util libraries, and run a **visualizer** to see **duplicates** and **candidates** to mark **externals** in library builds. The **`react` package** is usually not your largest chunk—**data**, **i18n**, and **charts** often dominate.\n",
        "examples": [E("Targeted import", "import debounce from 'lodash/debounce';\n", "Smaller than `import * as _ from 'lodash'` when tree-shake cannot prove the cut.", "tsx")],
        "tip": "Compare **before/after** gzip on CI for dependency upgrades so regressions are caught in review.\n",
        "links": L("Vite: build options", "https://vitejs.dev/config/build-options.html"),
    },
    {
        "id": "react-076",
        "question": "Can you use custom elements (web components) inside React?",
        "difficulty": "intermediate",
        "category": "interoperability",
        "tags": ["web-components", "custom-elements", "interop"],
        "answer": "Yes. A **lowercase** tag in JSX (for example **`<x-map />`**) is an **intrinsic** **custom** element. React 19+ passes most attributes through to **DOM** properties; **kebab** attributes and **custom events** may still be easier to wire with a **`ref` effect** and **`addEventListener`** for **CustomEvent** shapes your wrapper does not map yet.\n",
        "examples": [E("Render + ref effect", "useEffect(() => {\n  const n = r.current;\n  if (!n) return;\n  const h = () => {};\n  n.addEventListener('item-select', h);\n  return () => n.removeEventListener('item-select', h);\n}, []);\n", "Imperative bridge when a web component’s event is not a simple `onX` in JSX.", "tsx")],
        "tip": "Prefer a thin **React** wrapper with a **typed** props table so app teams do not re-learn the custom element for every use.\n",
        "links": L("MDN: Using custom elements", "https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements"),
    },
    {
        "id": "react-077",
        "question": "How do you use `ResizeObserver` in a React app?",
        "difficulty": "intermediate",
        "category": "hooks",
        "tags": ["resize", "observer", "useEffect"],
        "answer": "Create **`const ref = useRef<HTMLDivElement>(null)`**, then in **`useLayoutEffect` or `useEffect`**, if `ref.current` exists, `new ResizeObserver` with a callback that **`setState`**s measured **width/height** from `entry.contentRect`. **Cleanup** must **`disconnect()`** the observer. **Pick `useLayoutEffect`** when child layout depends on the **measured** size in the same frame; otherwise `useEffect` is enough.\n",
        "examples": [E("Measure box", "const [w, setW] = useState(0);\nconst r = useRef<HTMLDivElement>(null);\nuseLayoutEffect(() => {\n  if (!r.current) return;\n  const o = new ResizeObserver(([e]) => setW(e.contentRect.width));\n  o.observe(r.current);\n  return () => o.disconnect();\n}, []);\n", "Updates when the parent layout changes the element’s size.", "tsx")],
        "tip": "Debounce with **`requestAnimationFrame`** if the observer spams (some browsers coalesce, but not always).\n",
        "links": L("MDN: ResizeObserver", "https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver"),
    },
    {
        "id": "react-078",
        "question": "How can you pretty-print or safely display JSON in React?",
        "difficulty": "beginner",
        "category": "patterns",
        "tags": ["json", "debug", "xss"],
        "answer": "For a **read-only** panel, render **`JSON.stringify(data, null, 2)`** inside a **`<pre>`** (with `overflow: auto` for long bodies). The output is **text**, not HTML, so you avoid the **`innerHTML`**. For very **large** trees, **truncate** or a **“copy”** button is friendlier than rendering megabytes in the DOM.\n",
        "examples": [E("Debug readout", "export function JsonDebug({ d }: { d: unknown }) {\n  return <pre>{JSON.stringify(d, null, 2)}</pre>;\n}\n", "Replace with a highlighter in prod docs sites; for internal tools this is often enough.", "tsx")],
        "tip": "If `d` can contain **PII**, gate this component behind **auth** and **mask** before stringify.\n",
        "links": L("MDN: JSON.stringify", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify"),
    },
]

if __name__ == "__main__":
    Path(ROOT / "seed_71_78.json").write_text(json.dumps(ITEMS, indent=2) + "\n", encoding="utf-8")
    print("wrote", len(ITEMS))
