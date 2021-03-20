import click
import simulation_tracker
import click.testing
import pytest

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_click_in_general(runner):
    @click.command()
    def test_command():
        """Test fun for click.
        """
        click.echo('Test Test.')
    result = runner.invoke(test_command, ['--help'])
    assert not result.exception
    assert 'Test fun' in result.output, "Click did not deliver expected help out."

def test_tracker_command(runner):
    @simulation_tracker.track_command()
    @click.option('--test', type=int, help='Temperature of the command.')
    def test_tracker_command(test):
        """Test function for tracker command.
        """
        click.echo('Setting T.')

    # Test the help output
    result = runner.invoke(test_tracker_command, ['--help'])
    assert not result.exception
    assert 'Test function' in result.output, "Did not get the correct help output"
    assert '--test' in result.output, "Did not get the correct help output"

    # Test options
    result = runner.invoke(test_tracker_command, ['--test', '1'])
    assert not result.exception, result.output
    assert 'Setting T' in result.output, f"Option not working properly, {result.output}."
