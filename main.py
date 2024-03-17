import jygo

def Main() -> Exception:
    try:
        import jygo.package.log.pkg as log
        log.m()
    except Exception as e:
        return e
    else:
        return None

script = jygo.Script()
script.setMain(Main)
script.run()