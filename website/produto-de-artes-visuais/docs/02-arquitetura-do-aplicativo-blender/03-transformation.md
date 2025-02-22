# Transformation

## Blender's transformation
- An important concept of ***Blender Arquitecture***.
- ***Blender's transformation engine***
    - Based on the ***principle of generality***.
    > Instead of working on specific data types, transformation occurs on ***transform-specific abstract data structures*** that hold all the information needed for each specific transformation to do its job on all the *Blender Data Types* that would support it.
    - So we have a generic structure for Move, Rotate and Scale, for example.
    > Em resumo: Temos uma estrutura genérica para transformation. Esta estrutura pode ser usada por todos os data types de objetos do Blender. Mas um objeto tem  que suportar requisitos definidos pela estrutura genérica para pode usar tal estrutura genérica de transform.
- Transformations refer to a number of operations that can be performed on a selected Object or Mesh. Operations that alter the position or characteristics of the selected object.
- Each object can be moved, rotated and scaled in Object Mode. However, not all of these transformations have an effect on all objects. For example, scaling a camera has no effect on the render dimensions.
- Transform controls
    - Transform controls can be used to modify and control the effects of the available transformations.
- The transform constraint system is also generic: axis selection and basic spacial adjustment (correction for viewport and perspective) functions are defined once, each transformation function has to define how to apply it from the axis definitions.
    - Same for numerical input (which supports N-axis input).

### Basic transformations:
- Move
- Rotate
- Scale

### Advanced transformations:
- Move/Scale Texture Space tool
    - It transforms the Texture Space of the object

### General structure for transformation
- Important structures are all defined in ***source/blender/include/transform.h***.
    - **TransInfo** : Represents the transform engine. All global transformation flags and settings are stored in here. This structure is passed to each transform function call.
    - **TransData** : Represents a single transformation unit (a vertex, a CV, an object, ...)
    - **TransDataExtension** : Holds additional information tied to TransData units (in the case of objects, this holds rotation and size information)
    - **TransData2D** : Represents 2D Transformation units. These are used when flushing the transformation back to the 2D data, the actual transformations are done on TransData.
    - **NumInput** : Contains data needed by the Numerical input system (pretty much standalone)
    - **TransSnap** : Contains data needed by the snapping system

### Call Flow
- ***Public interface (calls) to the transformation engine***
    - Defined in **source/blender/include/BIF_transform.h**.
    - It is kept purposefully **very simple**.

- The principal calls are initTransform(mode, context) which sets up the engine (data conversion, center and proportional editing (PET) calculations, transformation specific setup, ...) and Transform() which runs the actual transformation.

For the initialization call, mode corresponds to the transformation to execute and context refers to specific restrictions that can be applied to the transformation or that might precise on which data it needs to act if the global Blender context isn't clear enough. (constants for context flags and modes are also defined in this header)

The same pair of init/action functions exists for the manipulator (initManipulator and ManipulatorTransform) with the difference that the init function doesn't have a context argument (for lack of use, it might be added later if it is needed).

Drawing callbacks are defined for the manipulators, the PET circle of influence, the constraints guidelines and snapping target.

Setup calls for the constraints system exists and must be called after the transform initialization call and, obviously, before the action call.


Inner Workings
Here's a quick overview of the inner call flow when public calls are received.

Initialization
Global initialization: initial mouse position, 3D view orientation save, global flags cleared
Per transform mode flags setup: setup restrictions to numinput and constraints if needed
TransData creation: depending on the Blender context, specific data is extracted from selection and converted to TransData for later manipulation.
Select what data type to convert
Extract all or only selected data (depending on PET tool)
Convert to TransData: This involves saving initial value for location and other specific properties (tilt for curves), creating TransDataExtension for data types that need it.
Initialize Snapping Engine
Calculate PET factors per TransData units if needed
Calculate transformation Center depending on the center mode selected by the user
Per transform mode initialization: this involves setting the function pointer corresponding to the actual transformation mode that will be applied, setting up "gears" step values (Ctrl / Shift), numerical input restrictions and other specific values
Main Action Loop
This is basically a loop polling for UI events, calling the transform mode functions and doing cleanups once everything is done

Transformation loop
Check mouse position, if it moved, raise the redraw flag
If redraw flag is raised, call the transform mode function
Poll for event, call the events treatment functions for each: that treatment function will dispatch events to the numerical input and snapping system for further treatment after trying to act on events itself
If state is CANCEL, roll back transformation using saved information in TransData and TransDataExtension (when present)
Free transformation data structures
Special post transform Blender updates (base flags, keyframe inserts, Actions insert, ...)
Push undo if needed
Transform Mode function
These are usually pretty simple. From the saved mouse pointer data, derive a transformation vector/factor/angle, loop on all TransData units and apply it. Here's a typical implementation (ToSphere). Others might be more or less complex. Steps in bold are rather mandatory.

Use a generic input method to derive motion (InputHorizontalRatio)
Snap value to the "grid/gears" steps
Apply numerical input
Create output string for header
Apply transformation to all TransData units
recalcData : Flush updates to Blender data when needed
headerPrint : Send text to the header
viewRedrawForce : Send redraw events to the proper screen area