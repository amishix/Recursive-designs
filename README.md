##Recursive Design with Python Turtle

A collection of recursion sketches built with Python’s turtle module, including fractal-style trees (with leaves and apples) and a tri curve pair that creates a mirrored, rhythmic pattern. This README explains the project, how it works conceptually, and gives step-by-step instructions to run and customise everything.

---

## Previews

## Fractal Trees
![Fractal trees preview](https://github.com/amishix/Recursive-designs/blob/c051ad33fd63ed7925e58f10655e3bdf88b357f7/recursive%20designs%20/Trees/recursivetrees.jpg)

### Tri Curve
![Tri curve preview](https://github.com/amishix/Recursive-designs/blob/main/recursive%20designs%20/curves/3.jpg)

---

## What’s inside

- `trees.py` – draws:
  - a grass foreground
  - a randomised branching tree
  - a leaf-cluster tree variant
  - an apple tree variant
- `curves.py` – draws:
  - a tri curve using recursive turns
  - a mirrored reverse tri curve for a layered effect
- `images/` – place screenshots here and reference them in `README.md`.

---

## Prerequisites

- **Python 3.8+** installed
- The **turtle** module comes with standard Python on Windows and macOS.  
  - On some Linux setups you may need Tk support: `sudo apt-get install python3-tk`.

---

## Getting started

1. **Clone or open your repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Create the images folder** for screenshots
   ```bash
   mkdir -p images
   ```

3. **Add your code files**
   - Save your tree code as `trees.py`.
   - Save your tri curve code as `curves.py`.

---

## How to run the tree sketches

1. **Run the script**
   ```bash
   # macOS/Linux
   python3 trees.py

   # Windows
   python trees.py
   ```

2. **What you will see**
   - The background turns orange.
   - A filled lime green rectangle is drawn as grass.
   - Three separate tree routines are drawn in sequence:
     - **Randomised branching tree**
     - **Leaf-cluster tree**
     - **Apple tree**

3. **Close the window**
   - When the drawing completes, close the turtle window to finish the programme.

### Customising trees

These variables control the look:

| Name  | Meaning | Typical values | Effect |
|------|---------|----------------|--------|
| `depth` | Recursion depth | 4 to 8 | Higher values = more branches |
| `dist` | Initial branch length | 150 to 350 | Longer starting trunk |
| `angle` | Branching angle | 40 to 90 | Wider canopy |
| `sf` | Scale factor per branch | 0.4 to 0.8 | Shrinks branches faster |
| `t.pensize(...)` | Branch thickness | 1 to 8 | Thicker trunks |
| colours | e.g. `"brown"`, `"green"`, `"#c91c1c"` | any | Tree colours |

Reproducible output: add at the top
```python
import random
random.seed(42)
```

---

## How to run the tri curve sketches

1. **Run the script**
   ```bash
   # macOS/Linux
   python3 curves.py

   # Windows
   python curves.py
   ```

2. **What you will see**
   - A recursive **tri curve** is drawn.
   - A mirrored **reverse tri curve** is then drawn.

3. **Close the window**
   - Close the turtle window when done.

### Customising curves

```python
# Forward curve
tri_curve(depth=2, dist=400, color="blue", width=2)

# Reverse curve
tri_curve_reverse(depth=8, dist=4000, color="red", width=3)
```

| Name | Meaning | Typical values | Effect |
|------|---------|----------------|--------|
| `depth` | Recursion depth | 1 to 10 | Higher depth increases detail |
| `dist` | Base segment length | 100 to 4000 | Bigger curves |
| `color` | Line colour | `"blue"`, `"red"` | Aesthetics |
| `width` | Pen width | 1 to 6 | Thicker lines |

---

## Adding screenshots to the README

```bash
mkdir -p images
git add images/trees.png images/tri-curve.png
git commit -m "Add preview screenshots"
git push
```

Reference them in README:
```markdown
![Fractal trees preview](images/trees.png)
![Tri curve preview](images/tri-curve.png)
```

---

## Suggested structure

```
.
├─ README.md
├─ trees.py
├─ curves.py
└─ images/
   ├─ trees.png
   └─ tri-curve.png
```

---

## Licence

MIT 

---

## Credits

Built with Python’s `turtle` module and recursion.
"""

