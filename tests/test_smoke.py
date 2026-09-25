from app.main import main


def test_main_runs(capsys):
    main()
    assert "init" in capsys.readouterr().out
