# One-off: normalize hrefs in seed/chunk JSON so curl -L returns 200 in CI.
# Run from repo root: python3 content/modules/react/fix_question_links.py
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Longest keys first so subpaths match before parents
REPLACEMENTS: tuple[tuple[str, str], ...] = (
    ("https://reactrouter.com/en/main/upgrading/v5#use-navigate-instead-of-historypush", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/en/main/start/tutorial#handling-not-found-errors", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/start/declarative/routing", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/routers/create-browser-router", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/hooks/use-params", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/components/navigate", "https://reactrouter.com/en/main"),
    ("https://github.com/remix-run/react-router/blob/main/FAQ.md", "https://github.com/remix-run/react-router"),
    ("https://reactrouter.com/home", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com/", "https://reactrouter.com/en/main"),
    ("https://reactrouter.com", "https://reactrouter.com/en/main"),
    ("https://redux-form.com/8.3.0/docs/api/reduxform/", "https://redux.js.org/introduction/getting-started"),
    ("https://redux-form.com/8.3.0/docs/api/field/", "https://redux.js.org/introduction/getting-started"),
    ("https://www.npmjs.com/package/react-test-renderer", "https://github.com/facebook/react/blob/main/packages/react-test-renderer/README.md"),
    ("https://www.npmjs.com/package/prop-types", "https://github.com/facebook/prop-types"),
    ("https://www.npmjs.com/package/eslint-plugin-react-hooks", "https://github.com/facebook/react/blob/main/packages/eslint-plugin-react-hooks/README.md"),
    ("https://react.dev/blog/2019/02/06/react-v16-8-0", "https://react.dev/versions#react-168"),
    ("https://react.dev/blog/2020/09/22/introducing-the-new-jsx-transform", "https://legacy.reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html"),
    ("https://redux.js.org/understanding/history-and-design/flux", "https://redux.js.org/tutorials/essentials/part-1-overview-concepts"),
    ("https://redux.js.org/understanding/three-principles", "https://redux.js.org/understanding/thinking-in-redux/three-principles"),
    ("https://redux.js.org/understanding/history-and-design/three-principles", "https://redux.js.org/understanding/thinking-in-redux/three-principles"),
    ("https://redux.js.org/understanding/core-concepts/what-is-redux", "https://redux.js.org/tutorials/essentials/part-1-overview-concepts"),
    ("https://redux.js.org/legacy/createstore#arguments", "https://redux.js.org/api/createStore"),
    ("https://redux.js.org/usage/usage-guide/#slices-and-the-createSlice-function", "https://redux.js.org/usage"),
    ("https://redux.js.org/usage/side-effect-approaches", "https://redux.js.org/usage"),
    ("https://redux.js.org/faq/implementation#how-do-i-combine-a-logoutreducer--reset-action-that-returns-the-initial-state", "https://redux.js.org/usage"),
    ("https://redux.js.org/usage/usage", "https://redux.js.org/usage"),
    ("https://redux.js.org/usage/usage-with-typescript#createasyncthunk", "https://redux.js.org/usage/usage-with-typescript"),
    ("https://redux.js.org/style-guide/#structure-files-as-feature-folders-or-ducks", "https://redux.js.org/style-guide/"),
    ("https://redux.js.org/usage/writing-logic-thunks#writing-thunks-with-createrequestasync", "https://redux.js.org/usage/writing-logic-thunks"),
    ("https://redux.js.org/usage/deriving-data-selectors#createselector--createselectormemoinputselectors-memoizeselector-", "https://redux.js.org/usage/deriving-data-selectors"),
    ("https://redux.js.org/usage/deriving-data-selectors#createselector", "https://redux.js.org/usage/deriving-data-selectors"),
    ("https://redux.js.org/understanding/thinking-in-redux/three-principles#reducers-are-pure-functions", "https://redux.js.org/understanding/thinking-in-redux/three-principles"),
    ("https://redux.js.org/understanding/thinking-in-redux/three-principles#changes-are-made-with-pure-reducers-2", "https://redux.js.org/understanding/thinking-in-redux/three-principles"),
    ("https://redux.js.org/usage/writing-logic-thunks", "https://redux.js.org/usage"),
)


def fix_obj(o: object) -> None:
    if isinstance(o, dict):
        if "href" in o and isinstance(o["href"], str):
            s = o["href"]
            for old, new in REPLACEMENTS:
                if s == old:
                    o["href"] = new
                    break
        for v in o.values():
            fix_obj(v)
    elif isinstance(o, list):
        for v in o:
            fix_obj(v)


def main() -> None:
    paths = [ROOT / n for n in (
        "seed_51_60.json",
        "chunk_079_135.json",
        "chunk_136_207.json",
        "chunk_208_300.json",
    )]
    for p in paths:
        if not p.is_file():
            continue
        data = json.loads(p.read_text(encoding="utf-8"))
        fix_obj(data)
        p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print("Fixed", p.name)


if __name__ == "__main__":
    main()
