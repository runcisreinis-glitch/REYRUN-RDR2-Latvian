extends SceneTree

func _initialize() -> void:
    TranslationServer.set_locale("lv")
    var checks: Dictionary = {
        "inventory/action": "Atvērt",
        "inventory/status": "Atvērts",
    }
    var failed := 0
    for context: String in checks:
        var actual := String(tr("Open", context))
        if actual != checks[context]:
            push_error("%s: expected %s, got %s" % [context, checks[context], actual])
            failed += 1

    var forms: Dictionary = {
        0: "diennakšu", 1: "diennakts", 2: "diennaktis", 9: "diennaktis",
        10: "diennakšu", 11: "diennakšu", 19: "diennakšu", 20: "diennakšu",
        21: "diennakts", 22: "diennaktis", 111: "diennakšu", 121: "diennakts",
    }
    for count: int in forms:
        var expected := "%d %s" % [count, forms[count]]
        var actual := String(tr_n("%d day", "%d days", count, "duration")) % count
        if actual != expected:
            push_error("Count %d: expected %s, got %s" % [count, expected, actual])
            failed += 1

    print("Latvian catalogue: %d contexts, %d integer counts, %d failures." % [
        checks.size(), forms.size(), failed])
    quit(1 if failed else 0)
