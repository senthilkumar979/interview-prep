import json
from pathlib import Path

L = lambda label, href: [{"label": label, "href": href}]
E = lambda title, code, exp, lang="tsx": {"title": title, "language": lang, "code": code, "explanation": exp}
ROOT = Path(__file__).resolve().parent

ITEMS: list[dict] = [
    {
        "id": "react-011",
        "question": "What is the difference between state and props?",
        "difficulty": "beginner",
        "category": "state-and-props",
        "tags": ["state", "props", "lifting"],
        "answer": "Props are data and callbacks a **parent** passes down. The child should treat them as **read-only** in the simple React model: to change a value owned by the parent, the child calls a **callback** the parent provided, or the parent updates its own state and re-renders with new props.\n\n**State** is data a component (or a hook) **owns** and changes with `useState` or `useReducer` when something internal should update the screen.\n\nIf two children need the same value, **lift** state to their nearest **common ancestor** and pass it as props. This is *lifting state up* on **react.dev**.\n",
        "examples": [E("Lifted state", "import { useState } from 'react';\n\nfunction Parent() {\n  const [n, setN] = useState(0);\n  return <Child value={n} onAdd={() => setN((c) => c + 1)} />;\n}\n", "Only Parent owns the number. Child receives value and a way to request an increment.")],
        "tip": "Before adding a second `useState` for the same fact in two places, name one owner and lift to that owner.",
        "links": L("React: Sharing state between components", "https://react.dev/learn/sharing-state-between-components"),
    },
    {
        "id": "react-012",
        "question": "What is the difference between HTML and React event handling?",
        "difficulty": "beginner",
        "category": "events",
        "tags": ["events", "jsx", "onSubmit", "className"],
        "answer": "In plain HTML, people sometimes use `onclick=\"...\"` (a string) or attach with `addEventListener`. In React, event props are **camelCase** (`onClick`, `onChange`) and you pass a **function**, not a string of code for the same pattern.\n\nUse **`onSubmit` on** `<form>` and **`e.preventDefault()`** when you handle submission in JavaScript, so both button clicks and the Enter key follow expected behavior. JSX also uses `className` and `htmlFor` instead of `class` and `for` in markup.\n",
        "examples": [E("Form submit", "function Form() {\n  function onSubmit(e: React.FormEvent<HTMLFormElement>) {\n    e.preventDefault();\n  }\n  return <form onSubmit={onSubmit}><button type=\"submit\">Save</button></form>;\n}\n", "prevents the browser from doing a full page navigation; adjust imports for your TypeScript setup.")],
        "tip": "Attach submit handling to the form, not only to the button, for better keyboard and assistive support.",
        "links": L("React: Responding to events", "https://react.dev/learn/responding-to-events"),
    },
    {
        "id": "react-013",
        "question": "What are synthetic events in React?",
        "difficulty": "intermediate",
        "category": "events",
        "tags": ["synthetic", "events", "async", "dom"],
        "answer": "A **synthetic event** is the event object your `onClick`, `onChange`, and similar props receive. It wraps the browser’s **native** event so behavior is more **consistent** across engines and can align with how React’s own **event and update** model works at a high level.\n\n**Async handlers:** if you `await` inside a handler, read values you need (for example the current `input` value) **into a variable before** the first `await`, so you are not using a field from the event after React has finished that tick of the handler in a way that is surprising in your environment.\n\nCheck **react.dev** and your **React version** for any historical notes about very old *event pooling* details in old posts; in modern apps the practical rule is: **read early, act after await with your copies**.\n",
        "examples": [E("Async-safe pattern", "async function onChange(e: React.ChangeEvent<HTMLInputElement>) {\n  const v = e.target.value;\n  await someApi(v);\n}\n", "Store the input value in a local variable before await so the async work uses a stable string.", "tsx")],
        "tip": "In strict typing projects, `ChangeEvent<HTMLInputElement>` and friends document what you have in a handler.",
        "links": L("React: Responding to events", "https://react.dev/learn/responding-to-events"),
    },
    {
        "id": "react-014",
        "question": "What are inline conditional expressions?",
        "difficulty": "beginner",
        "category": "jsx",
        "tags": ["conditional", "rendering", "ternary", "and"],
        "answer": "They are **JavaScript expressions inside JSX** that choose what to render: the **ternary** `cond ? a : b`, **logical AND** `cond && <Thing />`, or an **if** *before* the return that assigns to a variable.\n\nRules of thumb: use `&&` only when the left side is truly **boolean** (or you understand that `0` and other falsy values can **render** as text if you are not careful). Use a ternary when you need **both** branches. For larger trees, use `if`/`else` **before** `return` for readability.\n",
        "examples": [E("Ternary and &&", "function Panel({ show }: { show: boolean }) {\n  return (\n    <div>\n      {show ? <span>On</span> : <span>Off</span>}\n      {show && <aside>Extra</aside>}\n    </div>\n  );\n}\n", "Ternary picks between two branches. `show &&` renders only when `show` is true; watch falsy numbers like 0 with `&&`.")],
        "tip": "Extract big conditional UIs into a small child component or a variable above the return to keep JSX readable.",
        "links": L("React: Conditional rendering", "https://react.dev/learn/conditional-rendering"),
    },
    {
        "id": "react-015",
        "question": "What is the \"key\" prop and what is its benefit when used in arrays of elements?",
        "difficulty": "beginner",
        "category": "reconciliation",
        "tags": ["key", "lists", "reconciliation", "identity"],
        "answer": "The **`key`** is a special prop React uses to **match list items between renders** when you build **arrays** of siblings (often with `map`). It should be **stable** for a given row’s identity across that list’s lifetime—usually an **id** from data, not the **array index** if the list can reorder, insert, or delete rows.\n\n**Benefit:** correct **reconciliation** so state in a child (input focus, local state) stays with the **right row** when the list order changes. Bad keys (or index keys in a reorderable list) can cause **wrong updates** and subtle UI bugs.\n\n`key` is **not** passed as a normal prop to your component’s `props` in the usual way for your own function parameters; it is consumed by React for reconciliation (with the modern transform, you still pass it in JSX on the element you return from `map`).\n",
        "examples": [E("Stable id from data", "items.map((row) => <Row key={row.id} title={row.title} />);\n", "Use a business id for key when rows can reorder, insert, or delete.")],
        "tip": "Never use random `Math.random()` for key; it forces a full remount every render.",
        "links": L("React: Rendering lists (keys)", "https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key"),
    },
    {
        "id": "react-016",
        "question": "What is the Virtual DOM?",
        "difficulty": "beginner",
        "category": "reconciliation",
        "tags": ["virtual-dom", "elements", "tree"],
        "answer": "The **Virtual DOM** is a **nickname** for how people explain React: your components build a **lightweight in-memory tree of React elements** (plain objects describing the UI for one snapshot), not the live browser nodes yet. When **state** or **props** change, React runs your components again, forms a **new** element tree, and **compares** it to the last one so it can **apply a small set of updates** to the real **DOM** in a later step.\n\nThe important interview idea: you write **declarative** “what the UI should be”; React’s **reconciler** (implemented with **Fiber** in modern versions) does the mechanical work. Do not confuse this with the **Shadow DOM** (browser feature for encapsulation)—it is a different term.\n",
        "examples": [E("JSX returns an element description", "function Greet() {\n  return <p>Hello</p>;\n}\n", "The compiler turns JSX into `createElement` calls that produce element objects. React then reconciles and commits the real paragraph when needed.", "tsx")],
        "tip": "Tie “Virtual DOM” to **re-render when state changes** and **reconciliation**—not to a magic guarantee that React is always the fastest for every use case.",
        "links": L("React: Render and commit", "https://react.dev/learn/render-and-commit"),
    },
    {
        "id": "react-017",
        "question": "How does the Virtual DOM work?",
        "difficulty": "intermediate",
        "category": "reconciliation",
        "tags": ["reconciliation", "commit", "render"],
        "answer": "In practice you can say: **(1) Render** — React calls your function components; they return a **new element tree** (a new snapshot) built from `createElement` / JSX. **(2) Reconciliation** — the reconciler **walks the new and previous trees** and figures out the minimal **changes** in its internal data structures (the Fiber tree). **(3) Commit** — React applies the needed **side effects to the real DOM** (or other hosts), runs layout and paint, and runs **effects** (`useLayoutEffect` then `useEffect`) in a defined order.\n\n**React 18+** can **batch** many state updates and use **concurrent** scheduling for some patterns so the browser stays responsive. The old phrase “diff the VDOM and patch the real DOM” is a **simplified** picture of the render → reconcile → **commit** pipeline the docs teach on react.dev.\n",
        "examples": [E("setState starts a re-render", "import { useState } from 'react';\n\nfunction Box() {\n  const [n, setN] = useState(0);\n  return <button onClick={() => setN(n + 1)}>{n}</button>;\n}\n", "Each click updates state. React re-renders, builds a new element tree, reconciles, and commits the new button text in the DOM when needed.", "tsx")],
        "tip": "If the interviewer says “go deeper,” name the three words **render, reconcile, commit** and point to the **render-and-commit** doc.",
        "links": L("React: Render and commit", "https://react.dev/learn/render-and-commit"),
    },
    {
        "id": "react-018",
        "question": "What is the difference between controlled and uncontrolled components?",
        "difficulty": "beginner",
        "category": "state-and-props",
        "tags": ["forms", "controlled", "uncontrolled", "ref"],
        "answer": "A **controlled** input (or other control) is one whose **value in the DOM** is always driven from **React state** (or store): you set `value={...}` and update state in `onChange` so the **single source of truth** is your state. An **uncontrolled** control keeps its **own** current value in the **DOM**; you read it when needed with a **`ref`** (for example on submit) instead of holding every keystroke in state.\n\n**When to use which:** use **controlled** for most app forms where you need **validation, formatting, disabling submit, and instant feedback**. Use **uncontrolled** for very simple one-off cases or when you integrate with a non-React **imperative** widget, if your team allows it.\n",
        "examples": [E("Controlled text field", "import { useState } from 'react';\n\nexport function Email() {\n  const [v, setV] = useState('');\n  return <input value={v} onChange={(e) => setV(e.target.value)} />;\n}\n", "State is the source of truth; every keystroke flows through `onChange`.")],
        "tip": "Mention the single source of truth and `defaultValue` for a **half-controlled** uncontrolled first render when people mix patterns by mistake.",
        "links": L("React: Controlling an input with a state variable", "https://react.dev/learn/reacting-to-input-with-state#controlling-a-component"),
    },
    {
        "id": "react-019",
        "question": "What is `React.Fragment` and when do you use it?",
        "difficulty": "beginner",
        "category": "jsx",
        "tags": ["fragment", "jsx", "key"],
        "answer": "A **Fragment** lets a component return **several siblings** without adding an **extra** wrapper DOM node. Use **short syntax** `<> ... </>` when you do not need a key. When you `map` a list and the Fragment is the top node, use **`<React.Fragment key={id}>...</React.Fragment>`** because the short form cannot take `key`.\n\n**Why it matters:** some layouts and CSS (flex, grid) break if you insert a meaningless `div` just to wrap items. A Fragment keeps the **tree of real DOM** clean.\n",
        "examples": [E("Short fragment", "function Row() {\n  return (\n    <>\n      <td>a</td>\n      <td>b</td>\n    </>\n  );\n}\n", "Two cells without a wrapping `<div>` in the table row.")],
        "tip": "If you need a `key` on a mapped group, the **explicit** `<Fragment key={...}>` form is the right tool.",
        "links": L("React: Fragment", "https://react.dev/reference/react/Fragment"),
    },
    {
        "id": "react-020",
        "question": "What is `createElement` and how does it relate to JSX?",
        "difficulty": "intermediate",
        "category": "jsx",
        "tags": ["createElement", "jsx", "compiler"],
        "answer": "`createElement` is a **function** in the `react` package that **builds a React element object**: it records the **type** (tag name or component), **props** (including `children`), and special fields like `key`.\n\n**JSX** is **syntax** your bundler (with TypeScript) **compiles** into calls like `createElement`—or, with the **automatic** JSX runtime, into `jsx` from `react/jsx-runtime` so you do not need to import `React` in every file just for the factory.\n\nYou rarely call `createElement` by hand in app code, but you might when the **type** is chosen at **runtime** from a variable, or when you build tools that emit elements without a JSX step.\n",
        "examples": [E("JSX and createElement (conceptual)", "import { createElement } from 'react';\n\n// <Greet who=\"Ava\" /> roughly becomes:\nconst el = createElement(Greet, { who: 'Ava' });\n", "Both the JSX and the `createElement` call describe the same Greet instance with a `who` prop—React reconciles the element object either way.", "tsx")],
        "tip": "In interviews, add that **capitalized** names in JSX mean “component,” **lowercase** means **host** built-ins like `div`—the compiler still turns them into `createElement('div', …)`.",
        "links": L("React: createElement", "https://react.dev/reference/react/createElement"),
    },
]



if __name__ == "__main__":
    Path(ROOT / "seed_11_20.json").write_text(json.dumps(ITEMS, indent=2) + "\n", encoding="utf-8")
    print("wrote", len(ITEMS))
