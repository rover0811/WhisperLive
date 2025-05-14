from whisper_live.client import TranscriptionClient

if __name__ == "__main__":
    try:
        client = TranscriptionClient(
            host='whisperlive-cpu-620597935007.us-central1.run.app',
            port=443,
            lang='ko',
            save_output_recording=True,
            model='tiny',
            use_wss=True
        )
        client("/Users/rover0811/PycharmProjects/WhisperLive/assets/audio.m4a")
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"오류: {e.__class__.__name__}: {e}")
