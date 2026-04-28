"""One-off generator: writes content/modules/react/questions.json (78 items)."""
import json
from pathlib import Path

def L(label: str, href: str):
    return [{"label": label, "href": href}]

L_LEARN = "https://react.dev/learn"
L_REF = "https://react.dev/reference/react"
L_REACTDOM = "https://react.dev/reference/react-dom"
L_ROOT = "https://react.dev/reference/react-dom/client/createRoot"
L_MEMO = "https://react.dev/reference/react/memo"
L_USEEFFECT = "https://react.dev/reference/react/useEffect"
L_US = "https://react.dev/reference/react/useState"
L_LAZY = "https://react.dev/reference/react/lazy"
L_SUSP = "https://react.dev/reference/react/Suspense"
L_ERROR = "https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary"
L_MDN_LABEL = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label"
L_MDN_A11Y = "https://developer.mozilla.org/en-US/docs/Learn/Accessibility/What_is_accessibility"
L_MDN_INNER = "https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML"
L_ESLINT_HOOKS = "https://react.dev/reference/eslint-plugin-react-hooks"
L_VITE_ENV = "https://vitejs.dev/guide/env-and-mode.html"
L_GOOGLE_GTAG = "https://support.google.com/tagplatform/answer/10086991"

# Pool of one link per question (single object); rotate official docs
QUESTIONS = []

def add(**kw):
    QUESTIONS.append(kw)

add(
  id="react-001", question="What is React, and what problems is it meant to help you solve?", difficulty="beginner", category="fundamentals",
  tags=["react", "ui", "components", "library", "declarative"],
  answer="React is a JavaScript library for building user interfaces. It helps you build interactive screens out of small reusable pieces called components. You describe what the UI should look like for a given state, and React takes care of updating the page efficiently. Facebook (Meta) maintains it, and the modern ecosystem usually pairs React 18+ with function components and hooks. It focuses on the view layer, not the whole back end.",
  examples=[{"title": "A tiny function component", "language": "tsx", "code": "function Welcome({ name }: { name: string }) {\n  return <h1>Hello, {name}</h1>;\n}\n", "explanation": "A component is a function that returns elements describing UI."}],
  tip="Mention the declarative model: you think in state and UI, not manual DOM pokes everywhere.",
  links=L("React: Learn", L_LEARN),
)
add(
  id="react-002", question="What is JSX, and how is it not the same as a plain HTML string?", difficulty="beginner", category="jsx",
  tags=["jsx", "syntax", "transpile", "babel", "swc"],
  answer="JSX is a syntax extension that looks like HTML in JavaScript. Under the hood, it compiles to plain JavaScript function calls (historically `React.createElement` or similar). It is not a browser language by itself, so a build tool compiles it. In JSX, some names differ from HTML, such as `className` for CSS classes, because `class` is a reserved word in JavaScript. You can embed any JavaScript expression in curly braces between tags.",
  examples=[{"title": "JSX expression", "language": "tsx", "code": "const n = 3;\nreturn <p>Count: {n}</p>;\n", "explanation": "Curly braces run JavaScript inside the markup."}],
  tip="In interviews, state that the bundler (Vite, webpack, and so on) transforms JSX to JavaScript for the browser.",
  links=L("Describing the UI with JSX", f"{L_LEARN}/describing-the-ui"),
)
add(
  id="react-003", question="What is the virtual DOM, and why is it useful in React apps?", difficulty="beginner", category="reconciliation",
  tags=["virtual-dom", "render", "performance", "tree"],
  answer="The virtual DOM is a lightweight in-memory description of the UI tree React builds from your components. On each update, React creates a new virtual tree, compares it with the previous one, and figures out the smallest set of real DOM changes to apply. This keeps updates predictable and can reduce wasteful work compared with manually changing many DOM nodes without a plan. It is an implementation detail, not something you read from in normal app code.",
  examples=[],
  tip="Pair this answer with a mention of the reconciliation process when the interviewer goes deeper.",
  links=L("Render and commit", f"{L_LEARN}/render-and-commit"),
)
add(
  id="react-004", question="In simple terms, how does React decide to refresh what you see on the screen?", difficulty="beginner", category="reconciliation",
  tags=["state", "render", "update", "commit"],
  answer="When state, props, or context used by a component change, React schedules a render. During render, your components run like pure functions and return a new tree of elements. Then React diffs the new virtual tree with the last one, applies needed DOM updates in the commit phase, and runs effects after paint when you used `useEffect` for side work. Batching in React 18 can group many state updates into one render in common cases, which is good for performance.",
  examples=[],
  tip="Mention: render (calculate UI) is separate from commit (update DOM) in mental models.",
  links=L("Render and commit", f"{L_LEARN}/render-and-commit"),
)
add(
  id="react-005", question="What is a component in React, and what is the common approach in modern React 18 codebases?", difficulty="beginner", category="components",
  tags=["components", "props", "functions", "class", "legacy"],
  answer="A component is a reusable block of UI logic. In modern code you almost always use function components, plus hooks like `useState` for state. Class components still work but are a legacy style for new features. A component should ideally be small, focused, and get its inputs through props, context, and hooks, not by reaching into random globals.",
  examples=[{"title": "Function component", "language": "tsx", "code": "type Props = { title: string };\n\nexport function Panel({ title }: Props) {\n  return <section><h2>{title}</h2></section>;\n}\n", "explanation": "Props flow in, JSX flows out; no `this` keyword in functions."}],
  tip="Saying you default to function components and hooks is what teams expect in 2024+ codebases.",
  links=L("Your first component", f"{L_LEARN}/your-first-component"),
)
add(
  id="react-006", question="What is the difference between props and state in React?", difficulty="beginner", category="state-and-props",
  tags=["props", "state", "immutability", "parent", "read-only"],
  answer="Props are inputs passed from a parent to a child. A child should treat them as read-only. State is data owned by a component (often via `useState` or `useReducer`). When state or props that affect a component change, the component re-renders. Parents pass props down, children raise events or callbacks to ask parents to change state, which can flow back down as new props.",
  examples=[],
  tip="Never mutate props objects in place; that breaks React assumptions and can hide bugs.",
  links=L("Passing props", f"{L_LEARN}/passing-props-to-a-component"),
)
add(
  id="react-007", question="What does it mean to lift state up, and when is it a good idea?", difficulty="beginner", category="state-and-props",
  tags=["state", "lifting", "sharing", "siblings"],
  answer="Lifting state means moving shared data to the nearest common parent so more than one child can read and update the same data through props and callback props. You do this when two or more components must stay in sync. If the state is only used inside one child, you keep it local. If a sibling or parent must react to the same data, you lift it until it is visible to everyone that needs it.",
  examples=[],
  tip="Name a concrete example, such as selected tab shared by a header and the body.",
  links=L("Sharing state between components", f"{L_LEARN}/sharing-state-between-components"),
)
add(
  id="react-008", question="What are keys in lists, and why can using the array index as a key be risky when items move?", difficulty="beginner", category="reconciliation",
  tags=["key", "list", "identity", "reorder"],
  answer="A `key` is a stable identifier React uses to match list items between renders. Keys help React know which item moved, was added, or was removed, so it can update the correct component instances. If you use the array index as a key, reordering, inserting in the middle, or sorting can make React think an item is still the same row when the underlying data really moved. That can break local state, animations, and focus. Prefer stable database ids when you have them.",
  examples=[],
  tip="If a list is static, never reorders, and has no per-row state, index keys are less dangerous but still not best practice.",
  links=L("Preserving and resetting state", f"{L_LEARN}/preserving-and-resetting-state"),
)

Path(__file__).resolve  # make linters happy

# stub - more rows appended
if __name__ == "__main__":
  out = Path(__file__).resolve().parents[1] / "content/modules/react/questions.json"
  out.write_text(json.dumps(QUESTIONS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
  print(len(QUESTIONS), "written to", out)
