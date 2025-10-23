اكتب دالة باسم `processStates` تحاكي آلة حالات بسيطة. تأخذ حالة أولية، قائمة أحداث، وقاموس انتقالات، وتُرجع الحالة النهائية.

قاموس الانتقالات: `{(state, event): next_state}`

**المطلوب:**

- الدالة تأخذ ثلاثة معاملات: `initial_state`, `events`, `transitions`
- الدالة تعالج الأحداث واحد تلو الآخر
- إذا لم يكن هناك انتقال محدد، ابق في الحالة الحالية
- الدالة تُرجع الحالة النهائية بعد معالجة جميع الأحداث

**مثال:**

```python
processStates(
    "idle",
    ["start", "stop"],
    {("idle", "start"): "running", ("running", "stop"): "idle"}
)
# يُرجع: "idle"

processStates(
    "off",
    ["turn_on"],
    {("off", "turn_on"): "on", ("on", "turn_off"): "off"}
)
# يُرجع: "on"
```
